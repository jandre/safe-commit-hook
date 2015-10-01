#!/usr/bin/env python

import os
import json
import subprocess
import re

DEFAULT_PATTERNS=os.path.expanduser('~/.safe-commit-hook/git-deny-patterns.json')

def make_exact_matcher(str):
    def m(target):
        return str == target
    return m 

def make_regex_matcher(pattern):
    prog = re.compile(pattern)
    def m(target):
        return prog.match(target) 
    return m 

def make_str_matcher(p):
    if p['type'] == 'regex':
        return make_regex_matcher(p['pattern'])
    elif p['type'] == 'match':
        return make_exact_matcher(p['pattern'])
        

def make_filename_matcher(p):
    def m(target_filename):
        t = os.path.basename(target_filename)
        return p['_match'](t)
    return m

def make_extension_matcher(p):
    def m(target_filename):
        _, file_extension = os.path.splitext(target_filename)
        file_extension = file_extension[1:]
        return p['_match'](file_extension)
    return m

def make_path_matcher(p):
    def m(target_filename):
        return p['_match'](target_filename)
    return m

def make_matcher(p):
    p['_match'] = make_str_matcher(p)

    if p['part'] == 'filename':
        return make_filename_matcher(p)
    if p['part'] == 'extension':
        return make_extension_matcher(p)
    if p['part'] == 'path':
        return make_path_matcher(p)

def read_patterns():
    matchers = []
    with open(DEFAULT_PATTERNS) as data_file:    
        data = json.load(data_file)
        for p in data:
            matcher = make_matcher(p)
            if matcher:
                p['matcher'] = matcher
                matchers.append(p)
        return matchers 

def match_patterns(patterns, files):
    for f in files:
        for p in patterns:
            if p['matcher'](f):
                print '\033[91m' + "[ERROR] Unable to complete git commit." + '\033[0m' 
                print "%s: %s" % (f, p['caption'])
                if p['description']:
                    print p['description']
                exit(1)


cmd='git diff --name-only --cached'
result = subprocess.check_output(cmd, shell=True)
files = result.split("\n")
patterns = read_patterns()
match_patterns(patterns, files)

exit(1)
