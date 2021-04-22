#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CARLA_VERSION=$(cat ${SCRIPT_DIR}/ros-bridge/carla_ros_bridge/src/carla_ros_bridge/CARLA_VERSION)

docker run \
 -p 2000-2002:2000-2002 \
 --runtime=nvidia \
 --gpus 'all,"capabilities=graphics,utility,display,video,compute"' \
 -e SDL_VIDEODRIVER='offscreen' \
 -v /tmp/.X11-unix:/tmp/.X11-unix \
 -it \
 carlasim/carla:$CARLA_VERSION \
 ./CarlaUE4.sh
