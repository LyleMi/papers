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


def genReadme():
    pass


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
    opts = parser.parse_args()
    papers = loadJson()

    # when need add new tag
    for i in papers:
        papers[i]['Reading Notes'] = []
        papers[i]['Slides'] = ''
        papers[i]['Code'] = ''
        # papers[i]['new keyword'] = '' # or []

    if opts.search:
        keyword = opts.search
        for i in papers:
            p = papers[i]
            if keyword in p['Title'].lower():
                print(beautify(json.dumps(p)))
            elif keyword in p['Tag']:
                print(beautify(json.dumps(p)))
    elif opts.add:
        nindex = len(papers) + 1
        title = input('Title?')
        author = input('Author (split with ",")?')
        org = input('Organization?')
        tag = input('Tag (split with "-")?')
        date = input('Date?')
        conference = input('Conference?')
        newpaper = {}
        newpaper["Title"] = title
        newpaper["Author"] = author
        newpaper["Org"] = org
        newpaper["Date"] = date
        newpaper["Tag"] = tag.split('-')
        newpaper["Conference"] = conference
        papers[nindex] = newpaper
        print('add', newpaper)
        dumpJson(papers)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
