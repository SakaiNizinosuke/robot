#!/usr/bin/env python

from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['hsr_perception'],
    package_dir={'': 'scripts'},
    requires=['rospy']
)

setup(**d)
