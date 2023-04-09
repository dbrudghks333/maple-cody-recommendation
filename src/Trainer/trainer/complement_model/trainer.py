from ..base_trainer import BaseTrainer
from ...models.complement_model.model import ComplementModel
from ...models.complement_model.data_loader import ComplementDataLoader, load_DataLoader, preprocess_raw_data
import json
import os
from typing import Optional
from dataclasses import dataclass

from torch.utils.tensorboard import SummaryWriter
import torch.optim as optim
from torch.optim import lr_scheduler
import torch
import torch.nn as nn
import time


@dataclass
class TrainerArguments:
    data_path: str = './mnt/data/json_data_result.json'
    batch_size: int = 32
    num_workers: int = 8
    tensorboard_path: str = f"./mnt/{time.strftime('%Y.%m.%d - %H:%M:%S')}"
    model_save_path: str = './mnt/models'
    gender: str = "female"
    parts: str = "face"
    saved_model_path: Optional[str] = None
    num_epochs: int = 3
    learning_rate: float = 0.001
    step_size: float = 20
    gamma: float = 0.1


class Trainer(BaseTrainer):
    def __init__(
        self,
        data_path: str,
        batch_size: int,
        num_workers: int,
        model_save_path: str,
        tensorboard_path: str,
        gender: str,
        parts: str,
        saved_model_path: Optional[str],
        num_epochs: int,
        learning_rate: float,
        step_size: float,
        gamma: float,
    ):
        super().__init__(
            tensorboard_path=tensorboard_path,
        )
        self.batch_size = batch_size
        self.gender = gender
        self.parts = parts
        self.num_workers = num_workers
        (
            self.data_loader,
            self.answer_dict
        ) = self.get_dataloader(data_path)
        self.num_epochs = num_epochs
        self.learning_rate = learning_rate
        self.step_size = step_size
        self.gamma = gamma
        tensorboard_path = os.path.join(
            tensorboard_path,
            f"{time.strftime('%Y.%m.%d - %H:%M:%S')}-{gender}-{parts}"
        )

        self.model_save_path = model_save_path
        if not os.path.exists(model_save_path):
            os.makedirs(model_save_path)
        with open(os.path.join(model_save_path, f"{gender}_{parts}_answer_dict.json"), "w") as f:
            json.dump(self.answer_dict, f, ensure_ascii=False, indent="\t")
        self.model = ComplementModel(
            num_result_classes=self.data_loader.class_num
        )
        self.writer = SummaryWriter(tensorboard_path)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        if saved_model_path is not None:
            self.model.load(saved_model_path)
        self.model.to(self.device)

    def get_dataloader(
        self,
        data_path: str,
    ) -> ComplementDataLoader:
        with open(data_path, "r") as f:
            raw_data: dict = json.load(f)
            data_set, class_num, answer_dict = preprocess_raw_data(
                raw_data=raw_data,
                parts=self.parts,
                gender=self.gender,
            )
            data_loader = load_DataLoader(
                data_set=data_set,
                batch_size=self.batch_size,
                num_workers=self.num_workers,
                class_num=class_num,
            )
        return data_loader, answer_dict

    def step(
        self,
        epoch: int,
        num_epochs: int,
        criterion,
        optimizer,
        scheduler,
    ) -> bool:
        phases = [
            "train",
            "valid"
        ]
        for phase in phases:
            if phase == 'train':
                data_loader = self.data_loader.train
                self.model.train()
            else:
                data_loader = self.data_loader.valid
                self.model.eval()

            running_loss = 0.0
            all_cnt = 0
            accept_cnt = 0

            for batch_idx, batch_sample in enumerate(data_loader):
                inputs = batch_sample["input"].to(self.device)
                answers = batch_sample["answer"].to(self.device).squeeze(dim=-1)

                outputs = self.model(inputs)
                loss = criterion(outputs, answers)
                optimizer.zero_grad()
                running_loss += loss.item()
                _, o_v = torch.max(outputs, 1)
                for o, answer in zip(o_v, answers):
                    if answer.item() == o.item():
                        accept_cnt += 1
                    all_cnt += 1

                loss.backward()
                optimizer.step()
                self.log_batch(
                    num_batch=len(data_loader),
                    loss=running_loss / (batch_idx + 1),
                    corr_exp=accept_cnt / all_cnt,
                    batch_size=self.batch_size,
                    phase=phase,
                    num_epochs=num_epochs,
                    epoch=epoch,
                    batch_idx=batch_idx,
                )

            self.log_step(
                epoch_loss=running_loss,
                epoch_acc_exp=accept_cnt / all_cnt,
                phase=phase,
                epoch=epoch,
                num_epochs=num_epochs,
            )
            scheduler.step()
            print(f"EPOCH [{epoch:3d}]: loss: {running_loss :.5f} // acc: {accept_cnt / all_cnt:.5f}")

    def save_model(
        self,
        epoch: int
    ):
        os.makedirs(self.model_save_path, exist_ok=True)
        model_save_path = os.path.join(
            self.model_save_path,
            f"complement_model_{self.gender}_{self.parts}_EPOCH_{epoch}.pt"
        )
        torch.save(
            self.model.state_dict(),
            model_save_path
        )

    def train(
        self,
    ):
        params = self.model.parameters()
        optimizer = optim.Adam(params, lr=self.learning_rate)
        scheduler = lr_scheduler.StepLR(optimizer, step_size=self.step_size, gamma=self.gamma)
        criterion = nn.CrossEntropyLoss().to(self.device)

        for epoch in range(self.num_epochs):
            early_stop = self.step(
                epoch=epoch,
                num_epochs=self.num_epochs,
                criterion=criterion,
                optimizer=optimizer,
                scheduler=scheduler,
            )
            if early_stop:
                break
            self.save_model(
                epoch=epoch
            )
