# Carla-ros-docker

Run Carla simulator and Carla-ROS bridge (ROS2 Foxy) inside docker containers.

## Prerequisites

A Linux machine with an Nvidia GPU and nvidia-docker2.

Check the instructions at

https://carla.readthedocs.io/en/latest/build_docker/

for acquiring the Carla docker image. The ros-bridge used in this repo is compatible with Carla 9.11. Once downloaded, you can try to run the Carla container (headless) by running 

```bash
./carla-docker-bash-run.sh
```

which runs the Carla docker image headless. Alternatively, you can run the simulator with a screen by running the 'carla-docker-run.sh' script.

## Ros-bridge

Next, clone this repository, which contains a subtree of the official carla-simulator/ros-bridge.git repo with some additional components, by

```bash
git clone --recursive https://github.com/lasuomela/ros-bridge-compose.git
```

The version of Ros-Bridge included in this repo is compatible with Carla 9.11, and runs ROS2 Foxy. You can update the Ros-Bridge components by running 

```bash
git subtree pull-all
```
if needed.

### Usage

First, build the docker image by navigating into the 'docker-display' directory an running

```bash
./build.sh
```

If the image is built correctly, you can run it by


```bash
./run.sh
```

Which will start the docker container. Inside the container terminal, run 

```bash
colcon build
```

which builds the ros packages. Next, source the necessary workspaces by

```bash
source "/opt/carla-ros-bridge/install/setup.bash"
source "/opt/carla/setup.bash"
source "/opt/ros/foxy/setup.bash" 
```

Next, launch the carla autopilot and navigation nodes by running

```bash
ros2 launch compose compose.launch.py
```
which starts the necessary nodes and brings up the Rviz visualization tool. Now, you can set navigation goals for the autopilot by using the '2D Goal Pose' tool of Rviz. However, first you have to change the topic to which the '2D Goal Pose' is publishing. Do this by right clicking the toolbar in which the '2D Goal Pose' button is located. From the menu that opens, click 'Tool properties'. In the resulting setting window, change the '2D Point Goal' topic from '/goal_pose' to '/carla/ego_vehicle/goal'. Now you should be ready to set navigation goals for the autopilot.

### Components

Besides the official Ros-Bridge components, the repository contains two additional directories, 'docker-display' and 'compose'. 

#### Docker-display
Docker-display is based on the original 'docker' directory of Ros-Bridge. The included Dockerfile has been modified so that it mounts the Ros-Bridge directory to allow making persisting changes to files from inside the running docker container. This allows using the docker container as a development environment. These changes are reflected in the 'run.sh' script which can be used to start the Ros-Bridge. The 'run.sh' script also has some additional modifications for forwarding the screen out of the docker container, which allows running GUI apps such as rviz inside the container.

#### Compose

The 'compose' directory is a ROS2 package which makes launching multiple ROS-bridge components more convenient. The version included in this repository launches the nodes that are necessary for a Carla autopilot that can be controlled using the Rviz tool or ros topics. The ROS nodes and packages to launch are defined in the 'compose.launch.py' file located in the 'compose/launch/' directory.


