from setuptools import setup, find_packages

setup(
    name='price_catalog',
    version='0.1.0',
    description='Manages price lists and finds the best deals',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': ['price_catalog=price_catalog.cli:main']
    },

    # metadata
    author='Ryno Terblanche',
    auther_email='',
    license=''
)
