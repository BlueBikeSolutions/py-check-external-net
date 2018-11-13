""" Check domains, IPs, and hosts to ensure they are "external" """
from setuptools import setup


with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('flask/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

github = 'https://github.com/bluebikesolutions/py-check-external-net'

setup(
    name = 'check_external_net',
    version = version,
    url = github,
    project_urls=OrderedDict((
        ('Documentation', github + '/blob/master/README.rst'),
        ('Code', github),
        ('Issue tracker', github + '/issues'),
    )),
    license = 'BSD',
    author = 'Ricky Cook',
    author_email = 'ricky.cook@bluebike.com.au',
    description = 'Check domains, IPs, and hosts to ensure they are "external"',
    long_description = readme,
    py_modules = ['check_external_net'],
    install_requires = (
        'publicsuffix2',
    ),
    classifiers = (
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
    ),
)

