from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

install_reqs = parse_requirements('requirements.txt')

setup(
    name = "lrs",
    version = "0.0.0",
    author = "ADL",
    packages=['lrs'],
    install_requires=[install_reqs],
)
