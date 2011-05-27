"""letterblox.py"""

from nltk.corpus import wordnet
import random
import itertools
from optparse import OptionParser


if '__main__' == __name__:
    usage = "usage: %prog word"
    parser = OptionParser(usage=usage)
    args = parser.parse_args()[1]

    if len(args[0]) < 6:
        parser.error('please specify a 6 letter word')

    word = args[0]
    big_list = []
    n = len(word)
    d = {6:5, 5:10, 4:20, 3:30}

    while n >=3:
        max = d[n]
        for x in itertools.permutations(word, n):
            word = ''.join(x)
            if max <= 0:
                break
            if len(wordnet.synsets(word)) > 0 and word not in big_list:
                max-=1
                big_list.append(word)
        n-=1

    print '%d words found:\n %s' % (len(big_list), big_list)


