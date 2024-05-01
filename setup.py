from setuptools import setup

setup(
    name='pso',
    version='0.1',
    description='A Particle Swarm Optimization implementation in Python',
    author='Paula Isabella Moreno, Juan Sebastián Rueda, Santiago Rocha',
    author_email=', , srochap@unal.edu.co',
    packages=['pso'],
    install_requires=['numpy',
        'setuptools>=61.0'],
    python_requires='>=3.6',
)