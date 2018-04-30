from setuptools import setup

setup(
    name='LandingAI',
    version='0.1',
    author='Ravin Kumar',
    packages=['landingai'],
    install_requires=['tensorflow==1.30',
                      'pillow==4.3.0',
                      'keras==2.0.2',
                      'numpy==1.13.3']
)
