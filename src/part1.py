'''
Created on Mar 22, 2013

@author: cfogelberg
'''
import logging
import pprint
from word_tag_counts import WordCounts

if __name__ == '__main__':
    logging.info('Beginning part 1')
    wtc = WordCounts(r'C:\Users\cfogelberg\python-repos\coursera-nlp-asgn1\resources\gene.train')
    pprint.pprint(wtc.counts)
    logging.info('Ending part 1')   