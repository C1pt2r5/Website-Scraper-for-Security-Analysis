# setup.py
from setuptools import setup, find_packages

setup(
    name="security_log_analyzer",
    version="1.0",
    description="An advanced security log analyzer CLI for Linux and Windows EVTX logs.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "requests",
        "python-evtx"
    ],
    entry_points={
        "console_scripts": [
            "log-analyzer=main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    include_package_data=True
)
