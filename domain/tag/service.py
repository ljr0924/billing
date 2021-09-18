# -*- coding: utf-8 -*-

"""
@author: liangjr
@time: 2021/9/13 17:31
"""

import time

from .repos import Repository
from .models import Tag

class TagService(object):

    def __init__(self, repo: Repository):
        self.tag_repo = repo

    def get_all(self):
        return self.tag_repo.all()

    def get_tag(self, id_):
        return self.tag_repo.get(id_)

    def create(self, name, group_name):
        tag = Tag(
            name=name,
            group_name=group_name,
            created_time=int(time.time()),
            updated_time=int(time.time()),
            is_deleted=0
        )
        self.tag_repo.create(tag)

    def update(self, tag: Tag):
        pass