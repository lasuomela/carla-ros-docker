
# Containerized Carla+ROS2


Run Carla simulator and Carla-ROS bridge (ROS2 Foxy) inside docker containers with the Carla autopilot.

## Prerequisites

A Linux machine with an Nvidia GPU and nvidia-docker2. Clone this repository and submodules using

```bash
git clone https://github.com/lasuomela/carla-ros-docker.git
git submodule update --init --recursive
```

## Build & Run the Carla simulator

In the 'docker' directory:

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

##  Build & Run the Ros-bridge

The ROS-bridge ans Scenario Runner for Carla are included as submodules of this repository. Build them by running 

```bash
./build-ros-bridge-scenario.sh
```
Then, you can start the ROS-bridge by running

```bash
./run-ros-bridge-scenario.sh
```
which will enter you into the container shell. 

Now, the 'ad-runner' directory is mounted into the docker container as a volume, meaning you can make persisting changes into the directory from inside the running container. This means that you should use the 'ad-runner' directory to store your development code. After making changes into the development code remember to run

```bash
colcon build
```
and

```bash
source /opt/ad-runner/install/setup.bash
```
in the container.

## Running the demos

There are two demos contained in the repo. In the first one, the navigation goals for the Carla autopilot are set manually in Rviz2 using the '2D Goal Pose' tool. This demo can be launched (make sure to start the Carla simulator first) by running

```bash
ros2 launch place_reg_ad goal_pose_demo.launch.py 
```
inside the running ros-bridge image. You might have to run the command twice if the first attempt crashes. Alternatively, you can use the Scenario Runner addon to make the car follow a route predefined in the FollowRoute.xosc OpenScenario definition file. This second demo can be launched by running


```bash
ros2 launch place_reg_ad carla_ad_demo_with_scenario.launch.py 
```
