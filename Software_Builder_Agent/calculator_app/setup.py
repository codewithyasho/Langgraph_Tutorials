from setuptools import setup, find_packages

setup(
    name="python-calculator-app",
    version="1.0.0",
    author="Python Calculator Team",
    description="A simple command-line calculator application",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'calculator=main:main',
        ],
    },
)