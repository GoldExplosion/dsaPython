import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsapy",
    version="0.0.0",
    author="GoldExplosion",
    author_email="jivitesh.vit@gmail.com",
    description="""
    Package With Basic Data Structures Implementation.
    """,
    url="https://github.com/GoldExplosion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Engineering",
        "Topic :: Engineering :: Data Structures",
    ],
    python_requires='>=3.6',
    install_requires=[
        ],
)
