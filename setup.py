import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fenix_library-analyzing",
    version="0.0.2",
    author="Shivanand Pattanshetti",
    author_email="shivanand.pattanshetti@gmail.com",
    description="The analysis library for the Fenix Installer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/rebornos-team/fenix/libraries/analyzing",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: POSIX :: Linux",
    ],
    packages=setuptools.find_namespace_packages(include=['fenix_library.*']),
    python_requires='>=3.6',
    install_requires=[
        'psutil',
        'fenix_library-running',
        'fenix_library-configuration'
    ]
)