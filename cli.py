#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import argparse


def loadJson():
    with open('papers.json', 'r') as fp:
        obj = json.load(fp)
    return obj


def dumpJson(papers):
    with open('papers.json', 'w') as fp:
        json.dump(papers, fp)


def genReadme():
    pass


def main():
    parser = argparse.ArgumentParser(
        description='description',
        usage='[options]',
        epilog='epilog')
    parser.add_argument(
        '-s', '--search', action="store_true", help='search'
    )
    parser.add_argument(
        '-a', '--add', action="store_true", help='add new paper for index'
    )
    parser.add_argument(
        '-k', '--keyword', metavar='keyword', default='',
        help='search keyword'
    )
    opts = parser.parse_args()
    papers = loadJson()

    if opts.search and opts.keyword:
        keyword = opts.keyword
        for i in papers:
            p = papers[i]
            if keyword in p['title'].lower():
                print(p)
            elif keyword in p['tag']:
                print(p)
    elif opts.add:
        nindex = len(papers) + 1
        title = input('title?')
        author = input('author (split with ",")?')
        tag = input('tag (split with "-")?')
        date = input('date?')
        conference = input('conference?')
        newpaper = {}
        newpaper["title"] = title
        newpaper["author"] = author
        newpaper["date"] = date
        newpaper["tag"] = tag.split('-')
        newpaper["conference"] = conference
        papers[nindex] = newpaper
        print('add', newpaper)
        dumpJson(papers)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
