# -*- coding: utf-8 -*-

"""
@author: liangjr
@time: 2021/9/13 17:31
"""

from typing import Any

from pymysql import Connection

from .models import Tag


class Repository(object):

    def all(self):
        raise NotImplementedError

    def get(self, id_: int) -> Any:
        raise NotImplementedError

    def create(self, model: Any) -> int:
        raise NotImplementedError

    def update(self, model: Any) -> int:
        raise NotImplementedError

    def delete(self, id_: int) -> int:
        raise NotImplementedError


class MysqlRepo(Repository):

    def __init__(self, conn: Connection):
        self.conn = conn

    def all(self):
        sql = "select * from billing_tag"
        return self.cursor.execute(sql)

    def get(self, tag_id: int):
        sql = "select * from billing_tag where id=%d"
        cursor = self.conn.cursor()
        return cursor.execute(sql, (tag_id, )).fetchone()

    def create(self, tag: Tag):
        sql = """
        insert into billing_tag(`name`, `group_name`, `created_time`, `updated_time`)
        values (%s, %s, %d, %d, 0)
        """
        self.cursor.execute(sql, (tag.name, tag.group_name, tag.created_time, tag.updated_time, ))

        return

    def delete(self, tag_id: int):
        sql = """
        update from billing_tag set is_deleted = 1 where id = %d
        """
        return self.cursor.execute(sql, (tag_id, ))

    def update(self, tag: Tag):
        sql = """
        update from billing_tag set name = %s, group_name = %s, updated_time=now() where id = %d
        """
        return self.cursor.execute(sql, (tag.name, tag.group_name, tag.id_, ))
