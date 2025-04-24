"""
Una libreria de python con funciones comunes para el desarrollo en python\n
desarrolladores: Kevin Campos\n
module kender®\n
"""

import os

def alert(text):
    '''
    -----
    ### > Alert \n
    Esta funcion genera una alerta por consola formateada y responsiva a el largo del texto por consola

    have fun - kender
    -----
    '''  
    aux = "─"
    fix = aux*(int(len(text)/2))
    print(f"┌{fix} •✧✧• {fix}┐")
    #print(f"-{fix}ALERTA{fix}- ")
    print(f"    { text }")
    print(f"└{fix} •✧✧• {fix}┘")
    print("")

def makeSpace(multiplier):
    '''
    ----
    ### > MakeSpace \n
    Esta funcion genera una linea diagonal en consola para separar contenidos
    recibe como parametro un numero X el cual multiplica al string "-----"

    have fun - kender
    ----
    '''  
    print("-----"*multiplier)


def google(text):
    """Example Google style docstrings.

    This module demonstrates documentation as specified by the `Google
    Python Style Guide`_. Docstrings may extend over multiple lines.
    Sections are created with a section header and a colon followed by a
    block of indented text.

    Example:
        Examples can be given using either the ``Example`` or ``Examples``
        sections. Sections support any reStructuredText formatting, including
        literal blocks::

            $ python example_google.py

    Section breaks are created by resuming unindented text. Section breaks
    are also implicitly created anytime a new section starts.

    Attributes:
        module_level_variable1 (int): Module level variables may be documented in
            either the ``Attributes`` section of the module docstring, or in an
            inline docstring immediately following the variable.

            Either form is acceptable, but the two should not be mixed. Choose
            one convention to document module level variables and be consistent
            with it.

    Todo:
        * For module TODOs
        * You have to also use ``sphinx.ext.todo`` extension

    .. _Google Python Style Guide:   
    http://google.github.io/styleguide/pyguide.html

    """
    os.system("start https://www.google.com/search?q=" + text)


