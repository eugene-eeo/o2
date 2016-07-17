import sys
from distutils.core import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['-v']

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='o2',
    version='0.1.0',
    py_modules=['o2'],
    scripts=['bin/o2-index'],
    install_requires=[
        'lsm-db==0.3.2',
    ],
    tests_require=['pytest'],
    cmdclass = {'test': PyTest},
)
