from setuptools import setup

package_name = 'motorikin_study_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, package_name + '.scripts'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Motorikin',
    maintainer_email='motorikin84@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'first_node = motorikin_study_pkg.scripts.first_node:main',
            'talker = motorikin_study_pkg.scripts.talker:main',
            'listener = motorikin_study_pkg.scripts.listener:main',
        ],
    },
)
