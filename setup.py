from setuptools import setup, find_packages

setup(
    name='lock',
    version='0.0.2',
    url='https://github.com/jirih/lock',
    packages=find_packages(),
    license='GPLv3',
    author='jirih',
    author_email='',
    description='Lock problem solver',
    long_description='Lock problem solver',
    long_description_content_type="text/markdown",
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'lock = lock.lock:main'
        ]
    }, install_requires=[
    ],

)
