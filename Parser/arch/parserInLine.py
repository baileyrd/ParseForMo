# -*- coding: utf-8 -*-

from parseObj import ParseObj


def main():
    file = b'C:\\tmp\\streamLined\\CxSEIPRIMOASET-ACTIONADO-181016-0930-42.pdf'
    temp = None
    
    stream = b'<</Contents 13 0 R/Type/Page/Resources<</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]/Font<</F1 2 0 R/F2 3 0 R/F3 4 0 R>>>>/Annots[5 0 R 6 0 R 7 0 R 8 0 R 9 0 R 10 0 R 11 0 R 12 0 R]/Parent 14 0 R/MediaBox[0 0 612 792]>>\n'
    temp = InLineParser(stream)

    result = temp.printResults()

class InLineParser(ParseObj):

    def __init__(self, line, startToken = b'/', endToken = b' '):
        self.startToken = startToken
        self.endToken = endToken
        self.reset(line, self.startToken, self.endToken)

    # def yieldParse(self, data):
    #     for item in str(data):
    #         print(str(item))


if __name__ == '__main__':
    main()