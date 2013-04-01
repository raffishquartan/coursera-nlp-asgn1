'''
This file is part of assignment 1 for Michael Collin's NLP Coursera 
course, 02-04/2013 (MCNLP).

MCNLP is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

MCNLP is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with MCNLP.  If not, see <http://www.gnu.org/licenses/>.

@author:     cfogelberg

@copyright:  2013 Christopher Fogelberg. All rights reserved.
        
@license:    GPL

@contact:    cfogelberg@gmail.com
@deffield    updated: Updated
'''
import logging
import nlp_helpers
import os

def main_function(argv):
    '''
    Executes part 2 of assignment 1
    
    /argv/ replicates functionality if called from command line, but is not
    actually used for anything
    '''
    

if __name__ == '__main__':
    tags = ['O', 'I-GENE'] # these could be parsed out when the TrainingFile is loaded, but who cares 
    test_file = raw_input(r'Enter test file (..\resources\gene.(dev|test)): ')
    key_file = raw_input(r'Enter key file (blank if none exists): ')
    eval_output_file = raw_input(r'Enter tagging output file (..\output\gene_(dev|test).p1.out): ')
    
    # First replace rare words in training file and regenerate counts file:
    tf = nlp_helpers.TrainingFile(r'..\resources\gene.train', tags)
    ifwc = nlp_helpers.InputFileWordCounts(r'..\resources\gene.train')
    tf.replace_rare_words(ifwc, 5, '_RARE_')
    tf.save(r'..\output\gene.replaced')
    os.system(r'C:\Python27\python.exe count_freqs.py ../output/gene.replaced > ..\output\gene.replaced.counts')
    
    # Next load regenerated counts file, test file and tag using viterbi alg:
    cf = nlp_helpers.CountsFile(r'..\output\gene.replaced.counts', tags)
    testf = nlp_helpers.TestFile(test_file)
    testf.tag_and_save_argmax(cf, eval_output_file)
    if key_file != '':
        os.system(r'C:\Python27\python.exe eval_gene_tagger.py ../resources/gene.key ../output/gene_dev.p1.out')
    else:
        print "No key file specified - evaluation not possible"