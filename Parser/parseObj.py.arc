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
from result import Result

def main():
    file = 'C:\\tmp\\streamLined\\CxSEIPRIMOASET-ACTIONADO-181016-0930-42.pdf'
    temp = None
    # with open(file,'rb') as f:
    temp = ParseObj(file, b'%PDF-',  b'%%EOF\n')
    result = temp.printResults()


class ParseObj(object):

    def __init__(self, file, startToken=b'', endToken=b''):
        self.reset(file, startToken, endToken)

    def reset(self, file, startToken, endToken):
        self.resetStartFound()
        self.raw_data = []
        self.file = file
        self.startToken = startToken
        self.endToken = endToken
        self.result = Result()
        self.results = []
        self.getRawData()
    
    def getRawData(self):
        try:
            with open(self.file, 'rb') as f:
                for line in f:
                    self.raw_data.append(line)
        except Exception as e:
            pass
        finally:
            self.raw_data.append(self.file)


    def yieldParse(self, data):
        for line in data:
            if self.startToken in line:
                self.startFound = True
                self.result.start = line
            elif self.endToken not in line and self.startFound == True:
                self.result.content.append(line)
            elif self.endToken in line:
                self.result.end = line
                self.startFound = False
                yield 
    
    def resetStartFound(self):
        self.startFound = False
    
    def process(self):
        for obj in self.yieldParse(self.raw_data):
            # self.result.content.append(obj)
            yield obj
    
    def printResults(self):
        for result in self.process():
            self.results.append(result)
        
        print(len(self.results))
        # for item in self.results:
            # print(item.getValue())    



if __name__ == '__main__':
    main()