""" Check domains, IPs, and hosts to ensure they are "external" """
import pathlib
import re

from collections import OrderedDict
from setuptools import find_packages, setup


HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.rst').read_text()
VERSION = re.search(
    r"__version__ = '(.*?)'",
    (HERE / 'check_external_net/__init__.py').read_text(),
).group(1)

GITHUB = 'https://github.com/bluebikesolutions/py-check-external-net'

setup(
    name = 'check_external_net',
    version = VERSION,
    url = GITHUB,
    project_urls=OrderedDict((
        ('Documentation', GITHUB + '/blob/master/README.rst'),
        ('Code', GITHUB),
        ('Issue tracker', GITHUB + '/issues'),
    )),
    license = 'BSD',
    author = 'Ricky Cook',
    author_email = 'ricky.cook@bluebike.com.au',
    description = 'Check domains, IPs, and hosts to ensure they are "external"',
    long_description = README,
    packages = find_packages(),
    install_requires = (
        'publicsuffix2',
    ),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

