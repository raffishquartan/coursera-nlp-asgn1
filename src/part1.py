'''
common -- Commonly used snippets

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

if __name__ == '__main__':
    tf = nlp_helpers.TrainingFile(r'..\resources\gene.train')
    ifwc = nlp_helpers.InputFileWordCounts(r'..\resources\gene.train')
    tf.replace_rare_words(ifwc, 2, '_RARE_')
    tf.save(r'..\output\gene.replaced')
    
    cf = nlp_helpers.CountsFile(r'..\output\gene.train.counts')
    print cf['O Americans']
    print cf['O']