from setuptools import setup, find_packages

setup(
    name='beta4dist',
    version='0.2.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    description='A Python package for the Four-Parameter Beta Distribution and Likelihood-Based Estimation',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Soham Ghosh',
    author_email='phd2001161004@iiti.ac.in',
    url='https://github.com/soham39039820/beta4dist',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    python_requires='>=3.7',
    install_requires=[
        'numpy',
        'scipy'
    ],
    extras_require={
        'dev': ['pytest']
    },
)