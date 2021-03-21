#!/bin/env python3

import os
import xml.etree.ElementTree as ET

# -------------------------------------------------------------------------------------------------------------------- #

class BlogUser(object):
    def __init__(self, id: str, gender: str, age: str, activity: str, astro: str, data: str):
        self.id: int = int(id)
        self.gender: str = gender
        self.age: int = int(age)
        self.activity: str = activity
        self.astro: str = astro
        self.data: str = data

def parseBlogs(blogDir: str = 'blogs', blogCount: int = -1) -> list:
    blogUserList: list = []
    for blogFile in os.listdir(blogDir)[:blogCount] if blogCount >= 0 else os.listdir(blogDir):
        blogPath: str = f'{blogDir}/{blogFile}'
        with open(blogPath, encoding = 'ISO-8859-1') as blogFileContent:
            blogFileStr = blogFileContent.read().encode('ascii', errors = 'ignore')
            blogData: str = ''.join(post.text for post in ET.fromstring(blogFileStr).findall('post'))
        blogUserList.append(BlogUser(*blogFile.split('.')[:-1], blogData))
    return blogUserList