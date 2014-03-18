import os
from setuptools import setup

this_dir = os.path.dirname(__file__)
long_description = "\n" + open(os.path.join(this_dir, 'README.rst')).read()

setup(
    name='subprocess_check_output',
    version='0.0.0',
    description=('Adds subprocess.check_output to Python < 2.7'),
    long_description=long_description,
    author='Marc Abramowitz',
    author_email='marc@marc-abramowitz.com',
    py_modules=['subprocess'],
    zip_safe=False,
    install_requires=[],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ],
)
