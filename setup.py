from setuptools import setup

setup(
    name='seer',
    version='0.1',
    py_modules=['seer'],
    entry_points={
        'console_scripts': [
            'seer = seer:main',
        ],
    },
)
