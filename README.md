
# place-recognition-nav


Run Carla simulator and Carla-ROS bridge (ROS2 Foxy) inside docker containers with the Carla autopilot.

## Prerequisites

A Linux machine with an Nvidia GPU and nvidia-docker2. Clone this repository and submodules using

```bash
git clone https://github.com/lasuomela/carla-ros-docker.git
git submodule update --init --recursive
```

## Carla simulator

Pull the latest docker image compatible with the ROS-bridge master branch by running


```bash
./build-carla.sh
```

You can check

https://carla.readthedocs.io/en/latest/build_docker/

for more information about running the Carla docker image. Once downloaded, you can try to run the Carla container (headless) by running 

```bash
./run-bash-carla.sh
```

which runs the Carla docker image headless. Alternatively, you can run the simulator with a screen by running

```bash
./run-carla.sh
```

## Ros-bridge

The ROS-bridge for Carla is included as a submodule of this repository. Build it by running 

```bash
./build-ros-bridge.sh
```
Then, you can start the ROS-bridge by running

```bash
./run-ros-bridge.sh
```
which will enter you into the container shell. 

Now, the 'ad-runner' directory is mounted into the docker container as a volume, meaning you can make persisting changes into the directory from inside the running container. This means that you should use the 'ad-runner' directory to store your development code. By default, the ad-runner only contains a singe ROS package, 'compose', which is a convenience tool for launching multiple ROS-brige components at once. Launching the 'compose' package will start the ROS nodes needed for controlling the Carla autopilot using the Rviz visualization tool. Before we can run the packages, it has to be compiled. Do this after every change into your code sotred in 'ad-runner'. The compilation is initiated with

```bash
colcon build
```
which should be followed by

```bash
source /opt/ad-runner/install/setup.bash
```

Now, you can start the carla autopilot by running (make sure to start the Carla simulator first)

```bash
ros2 launch compose compose.launch.py
```
You might have to run the command twice if the first attempt crashes. After the nodes and Rviz GUI have been started you can set navigation goals for the autopilot by using the '2D Goal Pose' tool of Rviz. However, first you have to change the topic to which the '2D Goal Pose' is publishing. Do this by right clicking the toolbar in which the '2D Goal Pose' button is located. From the menu that opens, click 'Tool properties'. In the resulting setting window, change the '2D Point Goal' topic from '/goal_pose' to '/carla/ego_vehicle/goal'. Now you should be ready to set navigation goals for the autopilot.
