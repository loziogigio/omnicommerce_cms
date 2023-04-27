from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in omnicommerce_cms/__init__.py
from omnicommerce_cms import __version__ as version

setup(
	name="omnicommerce_cms",
	version=version,
	description="Cms to handle template section",
	author="Crowdechain s.r.o",
	author_email="developers@crowdechain.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
