#!/bin/bash

python -m src.InferenceServer \
    --model_json " \
        [ \
            [\"female\", \"hair\"], \
            [\"female\", \"cap\"], \
            [\"female\", \"faceAccessory\"], \
            [\"female\", \"face\"], \
            [\"female\", \"eyeAccessory\"], \
            [\"female\", \"earrings\"], \
            [\"female\", \"weapon\"], \
            [\"female\", \"longcoat\"], \
            [\"female\", \"shield\"], \
            [\"female\", \"pants\"], \
            [\"female\", \"cape\"], \
            [\"female\", \"shoes\"] \
        ]"