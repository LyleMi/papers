#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import argparse

from jsbeautifier import beautify


def loadJson():
    with open('papers.json', 'r') as fp:
        obj = json.load(fp)
    return obj


def dumpJson(papers):
    with open('papers.json', 'w') as fp:
        fp.write(beautify(json.dumps(papers)))

def reindex(papers):
    tmp = {}
    c = 1
    for i in papers:
        tmp[c] = papers[i]
        c += 1
    papers = tmp
    dumpJson(papers)
    return


def genReadme(papers):
    pc = {}
    conferences = set()
    for p in papers:
        if papers[p]['Conference'] not in pc:
            pc[papers[p]['Conference']] = []
        conferences.add(papers[p]['Conference'])
        pc[papers[p]['Conference']].append(papers[p])
    conferences = list(conferences)
    conferences.sort()

    with open('README.md', 'wb') as fh:
        for c in conferences:
            s = ''
            s += '# ' + c + '\n\n'
            s += '| '
            s += ' | '.join([
                'Title', 'Author', 'Organization', 'Year', 'Keywords'
            ])
            s += ' |\n'
            s += '|' + ' --- |' * 5 + '\n'
            for p in pc[c]:
                s += '| '
                s += ' | '.join([
                    p['Title'],
                    p['Author'],
                    p['Org'],
                    p['Date'],
                    ' '.join(p['Tag'])
                ])
                s += ' |\n'
            s += '\n'
            fh.write(s.encode('utf-8'))

def main():
    parser = argparse.ArgumentParser(
        description='description',
        usage='[options]',
        epilog='epilog')
    parser.add_argument(
        '-a', '--add', action="store_true", help='add new paper for index'
    )
    parser.add_argument(
        '-s', '--search', metavar='search', default='',
        help='search keyword'
    )
    parser.add_argument(
        '-g', '--gen', action="store_true", help='gen README'
    )
    opts = parser.parse_args()
    papers = loadJson()

    '''
    # when need add new tag
    for i in papers:
        # papers[i]['NewKeyword'] = '' # or []
        papers[i]['Abstract'] = '' # or []
        papers[i]['Comment'] = '' # or []
        if 'Reading Notes' not in papers[i]:
            papers[i]['Reading Notes'] = []
        if 'Slides' not in papers[i]:
            papers[i]['Reading Notes'] = ''
        if 'Code' not in papers[i]:
            papers[i]['Reading Notes'] = ''
    '''

    if opts.search:
        keyword = opts.search.lower()
        for i in papers:
            p = papers[i]
            if keyword in (json.dumps(p)).lower():
                # print(beautify(json.dumps(p)))
                print(p['Title'])
    elif opts.add:
        nindex = len(papers) + 1
        title = input('Title?').strip()
        author = input('Author (split with ",")?')
        org = input('Organization?').strip()
        tag = input('Tag (split with ";")?')
        date = '2019'
        date = input('Date?').strip()
        conference = 'BlackHat'
        conference = input('Conference?').strip()
        newpaper = {}
        newpaper['Title'] = title
        newpaper['Author'] = author
        newpaper['Org'] = org
        newpaper['Date'] = date
        newpaper['Tag'] = tag.split(';')
        newpaper['Conference'] = conference
        newpaper['Abstract'] = ''
        newpaper['Comment'] = ''
        newpaper['Reading Notes'] = []
        newpaper['Slides'] = ''
        newpaper['Code'] = ''
        papers[nindex] = newpaper
        print('add', newpaper)
        dumpJson(papers)
        genReadme(papers)
    elif opts.gen:
        genReadme(papers)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
