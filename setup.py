from setuptools import setup

packages = [
    'setcoverage',
]

test_requirements = ['pytest>=2.8.0', 'hypothesis==3.4.1']

version = '0.0.1'

setup(
    name='setcoverage',
    version=version,
    author='Conrad Dean',
    packages=packages,
    package_dir={'setcoverage': 'setcoverage'},
    zip_safe=False,
    tests_require=test_requirements,
)
