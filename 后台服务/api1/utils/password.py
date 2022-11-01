"""
# @Time    : 2022/10/20 16:26
# @Author  : violet
# @explain : 
"""

import hashlib

def md5(data: str) -> str:
    ha = hashlib.md5()
    ha.update(data.encode('utf-8'))
    return ha.hexdigest()