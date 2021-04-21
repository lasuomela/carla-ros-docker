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

XAUTH=/tmp/.docker.xauth
if [ ! -f $XAUTH ]
then
    xauth_list=$(xauth nlist :0 | sed -e 's/^..../ffff/')
    if [ ! -z "$xauth_list" ]
    then
        echo $xauth_list | xauth -f $XAUTH nmerge -
    else
        touch $XAUTH
    fi
    chmod a+r $XAUTH
fi

docker run \
    -it --rm \
    --net=host \
    --hostname $(hostname) \
    -e SDL_VIDEODRIVER='x11' \
    -e QT_X11_NO_MITSHM=1 \
    -e QT_QPA_PLATFORM='offscreen' \
    -e XAUTHORITY='$XAUTH' \
    --volume="$XAUTH:$XAUTH" \
    -e DISPLAY=${DISPLAY}\
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --mount 'type=bind,src=/home/lauri/Documents/ros-bridge/,dst=/opt/carla-ros-bridge/src/' \
    --gpus 'all,"capabilities=graphics,utility,display,video,compute"' \
    "$DOCKER_IMAGE_NAME:$TAG" "$@"

#docker run \
#    -it --rm \
#    --net=host \
#    -e SDL_VIDEODRIVER='x11' \
#    -e QT_X11_NO_MITSHM=1 \
#    -e XAUTHORITY='$XAUTH' \
#    --volume="$XAUTH:$XAUTH" \
#    -e DISPLAY=192.168.1.32:0\
#    -v /tmp/.X11-unix:/tmp/.X11-unix \
#    --mount 'type=bind,src=/home/lauri/Documents/ros-bridge/,dst=/opt/carla-ros-bridge/src/' \
#    --gpus 'all,"capabilities=graphics,utility,display,video,compute"' \
#    "$DOCKER_IMAGE_NAME:$TAG" "$@"
