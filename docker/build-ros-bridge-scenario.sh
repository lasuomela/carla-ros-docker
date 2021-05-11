#!/bin/sh

SCRIPT=$(readlink -f "$0")
SCRIPT_DIR=$(dirname "$SCRIPT")

ROS_DISTRO="foxy"

cd ${SCRIPT_DIR}/../ros-bridge/docker
./build.sh
cd ${SCRIPT_DIR}

docker build \
    -t carla-ros-bridge-scenario:$ROS_DISTRO \
    -f Dockerfile ${SCRIPT_DIR}/..
