###############################################################################
# aop-wiki_parser.py
#
# Lyle D. Burgoon, Ph.D.
# US Army Engineer Research and Development Center
#
# Version  1.0  Initial Write  2-23-2016
#
# Purpose: This module parses the AOP-Wiki JSON feeds
###############################################################################

import urllib.request
import json

json_out = urllib.request.urlopen('https://aopwiki.org/aops.json').read()
data = json.loads(json_out.decode("utf-8"))
print(data)





