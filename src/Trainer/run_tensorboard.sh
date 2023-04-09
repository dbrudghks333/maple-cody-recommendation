tensorboard --logdir=runs



aws ecr create-repository \
--repository-name make-train-data \
--image-scanning-configuration scanOnPush=true \
--region ${AWS_REGION}

aws ecr create-repository \
--repository-name tmp \
--image-scanning-configuration scanOnPush=true \
--region ${AWS_REGION}
