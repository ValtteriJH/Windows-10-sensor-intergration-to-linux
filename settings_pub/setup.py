from setuptools import setup

package_name = 'settings_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='teemu',
    maintainer_email='teemu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'freqPoints_settings = settings_pub.freqPoints_settings:main',
        'freqRange_settings = settings_pub.freqRange_settings:main',   
        'RBW_settings = settings_pub.RBW_settings:main',
        'txMode_settings = settings_pub.txMode_settings:main',
        ],
    },
)
