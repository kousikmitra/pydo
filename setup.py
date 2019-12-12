import setuptools

with open('requirements.txt') as f: 
    requirements = f.readlines() 

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydo", # Replace with your own username
    version="0.0.1",
    author="Kousik Mitra",
    author_email="kousikmitra12@gmail.com",
    description="A simple command line todo app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages() + ['static'],
    entry_points={ 
            'console_scripts': [ 
                'pydo = pydo.pydo:main'
            ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=requirements,
)