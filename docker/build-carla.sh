#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CARLA_VERSION=$(cat ${SCRIPT_DIR}/ros-bridge/carla_ros_bridge/src/carla_ros_bridge/CARLA_VERSION)
docker pull carlasim/carla:$CARLA_VERSION
