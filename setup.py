from setuptools import setup, find_packages

setup(
	name='gruselius',
	version='0.1',
	author='Joel G',
	author_email='joel.gruselius@scilifelab.se',
	url='',
	packages=find_packages(),
	scripts=['scripts/getting_data.py','scripts/check_repo.py'],
	license='GPLv3',
	long_description=open('README.md').read(),
	install_requires = ['untangle'],
)
