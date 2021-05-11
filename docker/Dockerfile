ARG ROS_DISTRO

FROM carla-ros-bridge:foxy

COPY ./scenario_runner /opt/scenario_runner
WORKDIR /opt/scenario_runner
RUN /bin/bash -c "pip3 install -r requirements.txt"
ENV SCENARIO_RUNNER_PATH="/opt/scenario_runner/"

COPY ./ad-runner /opt/ad-runner/src
WORKDIR /opt/ad-runner
RUN /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash; \
	colcon build"

COPY ./docker/install_additional_packages.sh /opt/install_additional_packages.sh
WORKDIR /opt/
RUN /bin/bash -c "bash /opt/install_additional_packages.sh"

WORKDIR /
RUN sed -i "s|exec "$@"|source /opt/ad-runner/install/setup.bash\nexec "$@" |g" ros_entrypoint.sh
