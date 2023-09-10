
# pysetting

![GitHub](https://img.shields.io/github/license/shiva-patt-oss/pysetting)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/shiva-patt-oss/pysetting)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pysetting?link=https%3A%2F%2Fpypi.org%2Fproject%2Fpysetting%2F)](https://pypi.org/project/pysetting/)
[![Release](https://github.com/shiva-patt-oss/pysetting/actions/workflows/release.yml/badge.svg)](https://github.com/shiva-patt-oss/pysetting/actions/workflows/release.yml)
[![Pre-Release (Git)](https://github.com/shiva-patt-oss/pysetting/actions/workflows/pre_release.yml/badge.svg)](https://github.com/shiva-patt-oss/pysetting/actions/workflows/pre_release.yml)

## Overview

A python library for parsing and storing settings and configurations.

**Warning**: This package is still in the Beta stage. It is not ready for production use. Please do not use for any critical software

<!-- ## [PLEASE CLICK HERE](https://github.com/shiva-patt-oss/pysetting/index.html) for the full documentation -->

## Cloning

In order to download the source code to your local computer for testing, or for development, you can clone from the remote repository using either SSH, or HTTPS. Below are instructions on how to do so using GitHub hosted code as remote.

### HTTPS

```bash
git clone https://github.com/shiva-patt-oss/pysetting.git 
```

OR

### SSH

```bash
git clone git@github.com:shiva-patt-oss/pysetting.git
```

## Packaging

Change to the project directory (`cd pysetting`) and run any of the below scripts:
- `sh packaging/setup.sh <MODE>`: Builds and installs a package
- `sh packaging/build-package.sh <MODE>`: Just builds a package without installing it locally
- `sh packaging/install-package.sh <MODE>`: Just installs a package locally, except if no built package is detected, a package is built.
 
OR

- `sh packaging_iso/setup.sh <MODE>`: Builds and installs a package
- `sh packaging_iso/build-package.sh <MODE>`: Just builds a package without installing it locally
- `sh packaging_iso/install-package.sh <MODE>`: Just installs a package locally, except if no built package is detected, a package is built.

where `<MODE>` can be one of the below
     1. `local`: Selects *pysetting-local* from the local project that you have cloned already.
     2. `git`: Selects *pysetting-git* from the latest git commit.
     3. `stable`: Selects *pysetting* from the git tag corresponding to the [`pkgver` specified in the PKGBUILD](https://github.com/shiva-patt-oss/pysetting/blob/main/packaging/pysetting/PKGBUILD#L17). If `pkgver=0.1.2`, then the git tag `v0.1.2` is used for packaging. 
     
> **Note**: Any additional parameters passed to the above scripts are automatically sent to `makepkg` or `pacman` (whichever is applicable).
