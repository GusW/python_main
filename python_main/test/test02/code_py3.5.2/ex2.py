'''
file        : ./ex2.py
test        : ./test.py
primary     : gustavo.watanabe@gmail.com
description : Write a library that supports validating and formatting post codes for UK.
              The details of which post codes are valid and which are the parts they consist of can be found at
              https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.
              The API that this library provides is your choice.
'''
from postcodemixin import PostcodeMixin


class Exercise2(PostcodeMixin):
    ''' Proposed solution to exercise 2 '''
    def postcode_API(self, postcode, region='UK', action='validates'):
        ''' API for both validation and formatting
            ATTENTION: only a few hardcoded special cases are covered
        '''
        return self.postcode_action(postcode, region, action)
