from setuptools import find_packages, setup

package_name = 'py_pkg'

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
    maintainer='marco',
    maintainer_email='marcoolivera096@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
             'pub = py_pkg.publisher:main',
            'sub =py_pkg.subscriber:main',
            'panel = py_pkg.led_panel:main',
            'ekf_pub = py_pkg.ekf:main',
            'move = py_pkg.move_robot:main',
            'test= py_pkg.test:main',
        ],
    },
)
