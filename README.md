# Carla-ros-docker
Dockerized Carla + Ros bridge

## Prerequisites

Check the instructions at

https://carla.readthedocs.io/en/latest/build_docker/

for acquiring the Carla docker image. The ros-bridge used in this repo is compatible with Carla 9.11. Once downloaded, you can try to run the Carla container (headless) by running the 'carla-docker-bash-run.sh' script, which runs the carla docker image headless. Alternatively, you can run the simulator with a screen by running the 'carla-docker-run.sh' script.

## Ros-bridge

Next, clone this repository, which contains a subtree of the official carla-simulator/ros-bridge.git repo with some additional components, by

```bash
git clone --recursive https://github.com/lasuomela/ros-bridge-compose.git
```

The version of Ros-Bridge included in this repo is compatible with Carla 9.11. You can update the Ros-Bridge components by running 

```bash
git subtree pull-all
```
if needed.

Besides the official Ros-Bridge components, the repository contains two additional directories, 'docker-screen' and 'compose'.




Build both docker images using the associated 'build.sh' scripts. Before building the Ros-bridge container, you might want to specify the desired python version for the ros bridge by setting the environment variable ROS_PYTHON_VERSION='3' or '2'.

To enable running GUI pygame applications from the ros-bridge container, it has to be added to the x11 access list by running 


```bash
xauth +local:
```

before the container is run the first time. To configure the x11 forwarding, modify the 'run.sh' script of ros-bridge so that the 'docker run' command includes the following arguments:

```bash
docker run \
    -it --rm \
    --net=host \
    -e SDL_VIDEODRIVER='x11' \
    -e DISPLAY=$DISPLAY\
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --gpus 'all,"capabilities=graphics,utility,display,video,compute"' \
    "$DOCKER_IMAGE_NAME:$TAG" "$@"
```


