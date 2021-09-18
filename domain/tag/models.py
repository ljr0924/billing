# -*- coding: utf-8 -*-

"""
@author: liangjr
@time: 2021/9/13 17:30
"""

from dataclasses import dataclass, field


@dataclass
class Tag(object):
    name: str  # 标签名称
    group_name: str  # 分组名称

    created_time: int  # 创建时间
    updated_time: int  # 更新时间
    is_deleted: int = field(default=0)  # 是否已删除
    id_: int = field(default=0)  # 主键id
