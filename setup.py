

from setuptools import find_packages, setup

setup(
    name='poetpy',
    version='1.0.0',
    author='Aaron Schlegel',
    author_email='aaron@aaronschlegel.com',
    description=('Python wrapper for the PoetryDB API.'),
    packages=find_packages(exclude=['docs', 'notebooks', 'tests*']),
    include_package_data=True,
    long_description=open('README.md').read(),
    install_requires=['requests >= 2.18'],
    home_page='',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
