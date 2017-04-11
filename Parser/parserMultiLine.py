# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

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
from parseObj import ParseObj

def main():
    file = 'C:\\tmp\\streamLined\\CxSEIPRIMOASET-ACTIONADO-181016-0930-42.pdf'
    temp = None
    # with open(file,'rb') as f:
    temp = MultiLineParser(file, b'%PDF-',  b'%%EOF\n')
    result = temp.printResults()    


class MultiLineParser(ParseObj):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self, file, startToken, endToken):
        self.reset(file, startToken, endToken)



    # def yieldParse(self, data):
    #     for line in data:
    #         print(type(line))
    #         print(type(self.startToken))
    #         if self.startToken in line:
    #             self.startFound = True
    #             self.result.start = line
    #         elif self.endToken not in line and self.startFound == True:
    #             self.result.content.append(line)
    #         elif self.endToken in line:
    #             self.result.end = line
    #             self.startFound = False
    #             yield self.result

 


if __name__ == '__main__':
    main()