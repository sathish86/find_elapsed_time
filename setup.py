from setuptools import setup, find_packages

import sys

from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(name='experiments_elapsed_time',
      version='0.1',
      description='Find experiments elapsed time from start and end dates',
      author='Sathish Kumar',
      author_email='sathish.cres07@gmail.com',
      license='MIT',
      packages=find_packages(),
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      install_requires=["pytest==5.0.1"],
      entry_points={
          'console_scripts': ['experiments_elapsed_time=experiments.command_line:main'],
      },
      zip_safe=False)
