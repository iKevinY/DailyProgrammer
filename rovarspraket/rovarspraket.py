# -*- coding: utf-8 -*-

import re

CONSONANTS_RE = re.compile('[b-df-hj-np-tv-z]', re.IGNORECASE)

def encode(msg):
    replacement = lambda m: m.group(0) + 'o' + m.group(0).lower()
    return re.sub(CONSONANTS_RE, replacement, msg)
