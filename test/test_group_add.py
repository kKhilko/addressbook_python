# -*- coding: utf-8 -*-

from model.group import Group


def test_group_add(app):
    old_group = app.group.get_list()
    app.group.create_new(Group(name="test", header="test_header", footer="test_footer"))
    new_group = app.group.get_list()
    assert len(old_group)+1 == len(new_group)

def test_group_add_empty(app):
    old_group = app.group.get_list()
    app.group.create_new(Group(name="", header="", footer=""))
    new_group = app.group.get_list()
    assert len(old_group)+1 == len(new_group)
