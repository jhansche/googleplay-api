from setuptools import setup

install_requires = ['requests', 'protobuf']
tests_require = []

setup(name='googleplay-api',
      version='1.0.0',
      description='Google Play Unofficial Python API',
      url='https://github.com/egirault/googleplay-api',
      py_modules = ['googleplay', 'googleplay_pb2'],
      author='egirault',
      install_requires=install_requires,
      tests_require=tests_require)
