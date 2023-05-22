from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in leave_app/__init__.py
from leave_app import __version__ as version

setup(
	name="leave_app",
	version=version,
	description="Modification of leave application",
	author="Abdalkarim Shehab",
	author_email="abdo.r.shehab2@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
