try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'William Fox',
    'url': 'https://www.github.com/foxwill/',
    'download_url': 'https://www.github.com/foxwill/',
    'author_email': 'williamfox[at]gmail[dot]com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
