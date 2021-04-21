#!/bin/sh

usage() { echo "Usage: $0 [-t <tag>] [-i <image>]" 1>&2; exit 1; }

# Defaults
DOCKER_IMAGE_NAME="carla-ros-bridge"
TAG="foxy"

while getopts ":ht:i:" opt; do
  case $opt in
    h)
      usage
      exit
      ;;
    t)
      TAG=$OPTARG
      ;;
    i)
      DOCKER_IMAGE_NAME=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done
shift $((OPTIND-1))

echo "Using $DOCKER_IMAGE_NAME:$TAG"

#    --mount 'type=bind,src=/home/lauri/Documents/carla-dev-stack,dst=/opt/carla-ros-bridge/src/' \

docker run \
    -it --rm \
    --net=host \
    -e SDL_VIDEODRIVER='x11' \
    -e DISPLAY=$DISPLAY\
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --mount 'type=bind,src=/home/lauri/Documents/ros-bridge/,dst=/opt/carla-ros-bridge/src/' \
    --gpus 'all,"capabilities=graphics,utility,display,video,compute"' \
    "$DOCKER_IMAGE_NAME:$TAG" "$@"
