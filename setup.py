import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fenix_library-analyzing",
    version="0.0.3",
    author="Shivanand Pattanshetti",
    author_email="shivanandvp@rebornos.org",
    description="A library for analyzing system specifications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/rebornos-team/fenix/libraries/analyzing",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "Typing :: Typed",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
        "Topic :: System :: Monitoring",
    ],
    packages=setuptools.find_namespace_packages(include=['fenix_library.*']),
    python_requires='>=3.6',
    install_requires=[
        'psutil',
        'fenix_library-running',
        'fenix_library-configuration'
    ]
)