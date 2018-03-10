'''
https://github.com/bartl3by/OXNote
'''

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='OXNote',
        version='0.1.4-dev',
        author='bartl3by',
        author_email='bartl3by@gmail.com',
        url='https://github.com/bartl3by/OXNote',
        license='GPLv3',
        description='OXNote is a desktop application for Open-Xchange AppSuite users designed for taking, organizing and sharing richtext notes. Notes created with OXNote will be stored on a remote Open-Xchange AppSuite account by using the OX Drive synchronization interface and are therefore accessible on all clients OXNote has been installed to.',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: MacOS X',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Operating System :: MacOS',
            'Operating System :: MacOS :: MacOS X',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3 :: Only',
            'Topic :: Text Editors :: Text Processing',
            'Topic :: Text Processing :: General'
        ],
        packages=["oxnote"],
        install_requires=['pyqt5',
                          'requests',
                          'urllib3',
                          'simplejson',
                          'keyring',
                          'qtpy',
                          'wheel',
                          'ruamel.yaml',
                          'python-slugify'],
        python_requires='>=3.6'
)
