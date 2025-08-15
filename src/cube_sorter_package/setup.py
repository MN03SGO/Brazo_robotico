from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'cube_sorter_package'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Tu Nombre',
    maintainer_email='tu_email@example.com',
    description='Robot clasificador de cubos por color',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_node = cube_sorter_package.nodes.camera_node:main',
            'vision_node = cube_sorter_package.nodes.vision_node:main',
            'control_node = cube_sorter_package.nodes.control_node:main',
        ],
    },
)