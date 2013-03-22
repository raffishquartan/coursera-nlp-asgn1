'''
Created on Mar 21, 2013

@author: cfogelberg
'''

import logging
import pprint

class WordCounts(object):
    '''
    Stores the word counts from a file and allows computation with them
    '''
    
    counts = {}

    def __init__(self, filename):
        '''
        Loads a WordTagCounts object from a counts file. Ignores n-grams. 
        '''
        try:
            with open(filename, 'r') as f:
                print "Opened file"
                for line in f:
                    self._load_wordtag(line.strip())
        except IOError as e:
            logging.error('Could not open {0}'.format(filename))
    
    def _load_wordtag(self, line):
        if len(line) != 0:
            word, tag = line.split()
            if word in self.counts:
                self.counts[word] += 1
            else:
                self.counts[word] = 1
    
    def counts(self, word):
        if word in self.counts:
            return self.counts[word]
        else:
            return 0