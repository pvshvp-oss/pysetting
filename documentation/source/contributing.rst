.. _contributing:

How to Contribute to Fenix Library - Analyzing
**********************************************

Testing
=======

.. todo::
    
    Add testing module
    Complete the documentation

1. Ensure that the instructions in :ref:`prerequisites` are followed.

2. 2. Install :code:`graphviz`, and :code:`fontconfig` for documentation generation

    .. code-block:: bash
            
        sudo pacman -S --needed graphviz fontconfig
  
3. Download the source from the *Git* repository
   
    .. code-block:: bash

        git clone https://gitlab.com/rebornos-team/libraries/analyzing.git
    
4. **Change to the downloaded directory** and run the below

    .. code-block:: bash

        sudo python -m pip install --force-reinstall dist/*.tar.gz

Development
===========

1. **Prerequisites**: Follow the instructions in :ref:`prerequisites`.
   
2. **API Documentation**: Consult :ref:`api_documentation` for an overview of the code.
   
3. **Git Repository**: *Fork* or *clone* the project from its **Gitlab** page and edit the source code of the project. For the *Git* URL, please refer to the **Testing** section above. 
   
4. **Code Editor**: Make sure that you have a code editor installed (like :code:`vscode`, :code:`atom`, :code:`gedit`, or an IDE like :code:`pycharm`). We recommend *VSCode* since if you open the file :code:`analyzing.code-workspace` (found in the directory :code:`analyzing/`) in *VSCode*, the :underlined:`recommended` *extensions* and *settings* are preconfigured to make your job easy and less error prone.

    .. code-block:: bash

        sudo pacman -S --needed code

5. After modifying the code, follow the **Testing** section above to test.
