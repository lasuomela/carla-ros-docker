#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CARLA_VERSION=$(cat ${SCRIPT_DIR}/ros-bridge/carla_ros_bridge/src/carla_ros_bridge/CARLA_VERSION)

xhost + local:
docker run \
  -e SDL_VIDEODRIVER=x11 \
  -e DISPLAY=$DISPLAY\
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -p 2000-2002:2000-2002 \
  -it \
  --gpus all \
  carlasim/carla:$CARLA_VERSION ./CarlaUE4.sh -openGL
xhost - local:

