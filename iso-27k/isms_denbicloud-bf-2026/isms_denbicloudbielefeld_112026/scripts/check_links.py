#!/usr/bin/env python3
"""
Small script for checking links/anker recursive within local md documents.

```
usage : python3 check_links.py <markdown>
```

Example checking complete ISMS markdown links/ankers: `python3 scripts/check_links.py index.md`
"""

import re
import sys

MAX_RECURSION_DEPTH = 10
VERBOSE = False

pattern_chapter = re.compile(r"^(#+)\s(.*?)$")
pattern_links =  re.compile(r"\[(.*?)\]\((.*?)(#(.*?))?\)")
pattern_extern_url = re.compile(r"^https?://")#

ankermap = {}
linkmap = {}


generate_anker_from_chapter = lambda a : a.lower().replace(' ','-').replace('(' ,'').\
    replace(')','').replace('/','').replace('.','').replace(',','')

def parse_and_check_file(filename,depth = 0):
    """ Parse a given md file and check linked (local) documents and anker."""

    def print(text):
        sys.stdout.write(f"{'#'*depth}: {text}\n")

    if depth > MAX_RECURSION_DEPTH:
        print(f"Maximum recursion depth reached {depth}")
        return

    # inital local data structures for found ankers and urls
    ankerset = set()
    urllist = []

    # read file ...
    try:
        file = open(filename, encoding="utf-8")
    except IOError as err:
        print(f"I/O error: {err}")
        sys.exit(1)

    lines = file.readlines()
    file.close()

    linenumber = 1
    # ... and iterate over it
    for line in lines:
        match = pattern_chapter.search(line)
        # search for a chapter (starting with '#')
        # and generate an anker representation from it
        if match  :
            anker = generate_anker_from_chapter(match.group(2))
            ankerset.add(anker)
        else:
            match2 = pattern_links.search(line)
            # search for a md link ('[text](url#anker)')
            if match2:
                url =  match2.group(2)
                anker = match2.group(4)
                urllist.append((url,anker,linenumber))
        linenumber += 1

    # save everything in global maps
    ankermap[filename] = ankerset
    linkmap[filename] = urllist

    # check links
    for url,anker,linenumber in urllist:

        # extern (starting with http[s])
        if pattern_extern_url.match(url):
            if VERBOSE:
                print(f"ignoring extern url ({url}) [{linenumber}]")
        else: # intern link
            # intern link is a md document
            if url.endswith(".md"):
                # if document is already parsed ..
                if url in ankermap :

                    if anker is not None and anker not in ankermap[url]:
                        print(f"Invalid anker ({url}#{anker}) [{filename}:{linenumber}]")
                        sys.exit(1)
                else:
                    # otherwise parse document
                    if not url.startswith("/"):
                        # adjust path when  having a relative url
                        parts = filename.split("/")
                        if len(parts) > 1 :
                            url = "/".join(parts[0:len(parts)-1])+"/"+url
                    if VERBOSE:
                        print(f"parse {url} [{linenumber}] ")
                    parse_and_check_file(url,depth+1)

if len(sys.argv) == 2:
    parse_and_check_file(sys.argv[1])
else:
    print(f"usage: {sys.argv[0]} <markdown>")
