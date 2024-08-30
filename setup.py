from setuptools import find_packages, setup

package_name = 'epuck_tof_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ks',
    maintainer_email='konstantin.stute@stud.tu-darmstadt.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'VL53L0X_node = epuck_tof_ros2.VL53L0X_node:main'
        ],
    },
)
