#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import argparse

from jsbeautifier import beautify


def loadJson():
    with open("papers.json", "r", encoding="utf-8") as fp:
        obj = json.load(fp)
    return obj


def dumpJson(papers):
    with open("papers.json", "w", encoding="utf-8") as fp:
        fp.write(beautify(json.dumps(papers, ensure_ascii=False)))


def reindex(papers):
    tmp = {}
    c = 1
    for i in papers:
        tmp[c] = papers[i]
        c += 1
    papers = tmp
    dumpJson(papers)
    return


def str2anchor(s):
    s = s.lower()
    s = s.replace(" ", "-")
    s = s.replace("/", "")
    s = s.replace("&", "")
    return s


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

    header = '''# Papers

Recently read academic papers, articles on Web Security/Fuzzing, etc., and some reading notes written by myself or excerpted from other sources.

## Table of Contents

- [Recommend Conferences](#recommend-conferences)
'''

    recommend = """
# Recommend Conferences

| Conference | Full Name | dblp Link |
| ----- | ----- | ----- |
| CCS | ACM Conference on Computer and Communications Security | https://dblp.uni-trier.de/db/conf/uss/ |
| Usenix | USENIX Security Symposium | https://dblp.uni-trier.de/db/conf/ccs/ |
| S&P | IEEE Symposium on Security and Privacy | https://dblp.uni-trier.de/db/conf/sp/ |
| NDSS | ISOC Network and Distributed System Security Symposium | https://dblp.uni-trier.de/db/conf/ndss/ |
"""

    footer = """## Disclaimer

To make the paper more accessible, please place the PDF version of the paper in the repo. All pdfs are collected from the Internet. If this article violates your copyright, please contact me to delete it.
"""

    with open("README.md", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(header)
        for c in conferences:
            fh.write("- [%s](#%s)\n" % (c, str2anchor(c)))
        fh.write(recommend)
        fh.write("\n")
        for c in conferences:
            s = ''
            s += '## ' + c + '\n\n'
            s += '| '
            s += ' | '.join([
                'Title', 'Authors', 'Organization', 'Year', 'Keywords'
            ])
            s += ' |\n'
            s += '|' + ' --- |' * 5 + '\n'
            pc[c].sort(key=lambda i: i["Title"])
            pc[c].sort(key=lambda i: i["Date"], reverse=True)
            for p in pc[c]:
                s += '| '
                s += ' | '.join([
                    p['Title'],
                    ';'.join(p['Author']),
                    p['Org'],
                    p['Date'],
                    ';'.join(p['Tag'])
                ])
                s += ' |\n'
            s += '\n'
            fh.write(s)
        fh.write(footer)


def main():
    parser = argparse.ArgumentParser(
        description="""
set default value:

set DATE=2020
set CONFERENCE=Usenix
""",
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
    for i in papers:
        if isinstance(papers[i]['Author'], str):
            papers[i]['Author'] = papers[i]['Author'].split(";")
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
                print(beautify(json.dumps(p)))
                print(p['Title'])
    elif opts.add:
        nindex = len(papers) + 1
        title = input('Title?').strip()
        author = input('Author (split with ";")?')
        org = input('Organization?').strip()
        tag = input('Tag (split with ";")?')
        # date = '2019'
        date = input('Date?').strip()
        if date == '':
            date = os.getenv('DATE')
        conference = input('Conference?').strip()
        if conference == '':
            conference = os.getenv('CONFERENCE')
        newpaper = {}
        newpaper['Title'] = title
        newpaper['Author'] = author.split(';')
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
