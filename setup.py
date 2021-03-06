try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python parser for AmiraMesh 3D ASCII 2.0 format',
    'author': 'Heikki Lehvaslaiho',
    'url': 'https://github.com/heikkil/amiramesh',
    'author_email': 'Heikki.Lehvaslaiho@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'data_files': ['data/lariat.am'],
    'packages': ['lib'],
    'scripts': ['bin/read_amiramesh.py'],
    'name': 'amiramesh'
}

setup(**config)
