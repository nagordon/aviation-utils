# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:06:54 2015

@author: ngordon

pip install wget
"""

import wget

airports = ['3g3','15g','67d']

for a in airports:
    file_url = 'http://www.aopa.org/airports/%s/kneeboard.pdf' % a
    file_name = wget.download(file_url)
    
