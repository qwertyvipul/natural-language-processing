# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 22:28:26 2019

@author: Vipul
"""

import nltk
"""
# Only once
nltk.download()
"""

from nltk.book import text1

# Concordance views show us every occurence of a given word, together with some context
text1.concordance("crooked")