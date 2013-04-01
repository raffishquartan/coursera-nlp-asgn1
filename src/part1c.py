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
import nlp_helpers

# Run this file after part1a and then running count.freqs on gene.replaced
if __name__ == '__main__':
    tags = ['I-GENE', 'O']
    cf = nlp_helpers.CountsFile(r'..\output\gene.replaced.counts', tags)
    testf = nlp_helpers.TestFile(r'..\resources\gene.test')
    testf.tag_and_save_argmax(cf, r'..\output\gene_test.p1.out')