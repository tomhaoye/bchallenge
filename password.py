#!/usr/bin/python

import os
from itertools import permutations

key = 'L30275849F'
ps = permutations(key)
for p in ps:
    try_p = ''.join(p)
    os.system(
        'openssl enc -aes-256-cbc -md md5 -d -in first_encrypt ' + ' -pass pass:' + try_p + ' >> big_out_file'
    )

f_password = 'L379F48502'
s_password = '02L3F95847'
