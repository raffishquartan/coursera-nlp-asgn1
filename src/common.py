'''
common -- Commonly used snippets

This file is part of Christo's commonly used Python components (CCUPC).

CCUPC is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CCUPC is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CCUPC.  If not, see <http://www.gnu.org/licenses/>.

@author:     cfogelberg
        
@copyright:  2013 Christopher Fogelberg. All rights reserved.
        
@license:    GPL

@contact:    cfogelberg@gmail.com
@deffield    updated: Updated
'''

def enum(**enums):
    '''
    Usage:
    Numbers = enum(ONE=1, TWO=2, THREE='three')
    assert Numbers.THREE == 'three' 
    '''
    return type('Enum', (), enums)

def enumseq(*sequential, **named):
    '''
    Usage:
    Numbers = enum('ZERO', 'FOO', 'TWO')
    assert Numbers.FOO == 1
    '''
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)