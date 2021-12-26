from setuptools import setup

setup(
    name='PyMax',
    extras_require=dict(test=['pytests']),
    packages=find_packages(where='src')
    package_dir={"":"src"},
)