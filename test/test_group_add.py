# -*- coding: utf-8 -*-
from sys import maxsize

from model.group import Group


def test_group_add(app):
    old_group = app.group.get_list()
    group =Group(name="test", header="test_header", footer="test_footer")
    app.group.create_new(group)
    new_group = app.group.get_list()
    assert len(old_group)+1 == len(new_group)
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)

def test_group_add_empty(app):
    old_group = app.group.get_list()
    group = Group(name="", header="", footer="")
    app.group.create_new(group)
    new_group = app.group.get_list()
    assert len(old_group)+1 == len(new_group)
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)