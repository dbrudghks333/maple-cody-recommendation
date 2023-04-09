aws ecr create-repository \
--repository-name wzcomparerr2server \
--image-scanning-configuration scanOnPush=true \
--region ${AWS_REGION}

