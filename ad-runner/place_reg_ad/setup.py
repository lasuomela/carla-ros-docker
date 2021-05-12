"""
Setup for carla_ad_demo
"""
import os
from glob import glob
ROS_VERSION = int(os.environ['ROS_VERSION'])

if ROS_VERSION == 1:
    from distutils.core import setup
    from catkin_pkg.python_setup import generate_distutils_setup

    d = generate_distutils_setup(
        packages=['place_reg_ad'],
    )

    setup(**d)

elif ROS_VERSION == 2:
    from setuptools import setup, find_packages

    package_name = 'place_reg_ad'
    setup(
        name=package_name,
        packages=find_packages(),
        version='0.0.0',
        data_files=[
            ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
             
            ('share/' + package_name, ['package.xml']),
            (os.path.join('share', package_name, 'config'), glob('config/*.xosc')),
            (os.path.join('share', package_name, 'config'), glob('config/*.rviz')),
            (os.path.join('share', package_name, 'config'), glob('config/*.json')),
            (os.path.join('share', package_name), glob('launch/*.launch.py'))
        ],
        install_requires=['setuptools'],
        zip_safe=True,
        maintainer='CARLA Simulator Team',
        maintainer_email='carla.simulator@gmail.com',
        description='CARLA ad demo for ROS2 bridge',
        license='MIT',
        tests_require=['pytest'],
        entry_points={
        'console_scripts': [
            'echo_node = place_reg_ad.echo_node:main'
        ],
        },
    )
    
       #         ('share/' + package_name + '/config',
        #     ['config/FollowRoute.xosc', 'config/place_reg_ad_ros2.rviz', 'config/objects.json']),
