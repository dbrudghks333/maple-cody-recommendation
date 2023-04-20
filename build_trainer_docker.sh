#!bin/bash
#
# docker build script

set -o pipefail

tag=$1
if [ -z $tag ]; then
  echo "please call bash script like 'bash build_trainer_docker.sh \$tag_name'"
  exit 1
fi

# TODO: change XXX to registry (ex ECR or ...)
REGISTRY="xxxx"
IMAGE_NAME="$REGISTRY/trainer:$tag"

echo "BUILD START: $IMAGE_NAME"

export DOCKER_BUILDKIT=1
docker build -f ./docker/Dockerfile.Trainer --network=host -t $IMAGE_NAME .
