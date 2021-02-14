# FENIX INSTALLER
# Please refer to the file `LICENSE` in the main directory for license information. 
# For a high level documentation, please visit https://gitlab.com/rebornos-team/fenix-installer

# AUTHORS
# 1. Shivanand Pattanshetti (shivanand.pattanshetti@gmail.com)
# 2. 

# IMPORTS
from .analyzing import * # since this package (analyzing) contains a single module (analyzing.py), flatten the module so that users can access items within the module analyzing.py by using just the package name (fenix_library.analyzing.item) instead of having to add the module name too (fenix_library.analyzing.analyzing.item)
