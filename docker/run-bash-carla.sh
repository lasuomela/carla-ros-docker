#!/bin/bash
SCRIPT=$(readlink -f "$0")
SCRIPT_DIR=$(dirname "$SCRIPT")
CARLA_VERSION=$(cat ${SCRIPT_DIR}/../ros-bridge/carla_ros_bridge/src/carla_ros_bridge/CARLA_VERSION)

docker run \
 -p 2000-2002:2000-2002 \
 --runtime=nvidia \
 --gpus 'all,"capabilities=graphics,utility,display,video,compute"' \
 -e SDL_VIDEODRIVER='offscreen' \
 -v /tmp/.X11-unix:/tmp/.X11-unix \
 -it \
 carlasim/carla:$CARLA_VERSION \
 ./CarlaUE4.sh /Game/Carla/Maps/Town01
