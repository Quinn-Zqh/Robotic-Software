from setuptools import setup

package_name = 'budding_yeast_description_pkg'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name + '/urdf', ['urdf/michael.urdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ZQH',
    maintainer_email='zhangqiuhui24@gmail.com',
    description='Example ROS 2 package for assessment',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)

