from distutils.core import setup

setup(
	name='gruselius',
	version='0.1',
	author='Joel G',
	author_email='joel.gruselius@scilifelab.se',
	url='',
	packages=['gruselius',],
	scripts=['scripts/getting_data.py',],
	license='GPLv3',
	long_description=open('README.md').read(),
	install_requires = ['untangle'],
)
