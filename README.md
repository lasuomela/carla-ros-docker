# Carla-ros-docker
Dockerized Carla + Ros bridge

## Prerequisites

Check the instructions at

https://carla.readthedocs.io/en/latest/build_docker/

for acquiring the Carla docker image. The ros-bridge used in this repo is compatible with Carla 9.11. Once downloaded, you can run the Carla container (headless) by

```bash
docker run \
 -p 2000-2002:2000-2002 \
 --runtime=nvidia \
 --gpus 'all,"capabilities=graphics,utility,display,video,compute"' \
 -e SDL_VIDEODRIVER='offscreen' \
 -v /tmp/.X11-unix:/tmp/.X11-unix \
 -it \
 carlasim/carla \
 ./CarlaUE4.sh
```

To run with a screen, just add 

```bash
  -e SDL_VIDEODRIVER=x11 \
  -e DISPLAY=$DISPLAY\
```
to the run directives.

## Ros-bridge

Next, clone the ROS bridge and checkout the latest stable version by

```bash
git clone --recursive https://github.com/carla-simulator/ros-bridge.git
```

You can switch to a stable version by checking out tags, for example

```bash
git checkout tags/0.9.10.1
```

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


