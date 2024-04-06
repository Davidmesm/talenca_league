from setuptools import setup, find_packages

setup(
    name='league-ranking',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'league-ranking = league_core.main:main'
        ]
    },
)
