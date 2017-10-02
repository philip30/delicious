from setuptools import setup, find_packages
import sys

sys.path.append("./delicious")

install_requires = [
  'numpy>=1.9.0',
  'Pillow',
]

setup(
  name='delicious',
  version='0.0.1',
  author='Philip Arthur',
  author_email='philip.arthur30@gmail.com',
  install_requires=install_requires,
  packages=[
      'delicious',
  ],
)
