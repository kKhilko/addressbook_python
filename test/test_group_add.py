# -*- coding: utf-8 -*-

from model.group import Group


def test_group_add(app):
    app.group.create_new(Group(name="test", header="test_header", footer="test_footer"))

def test_group_add_empty(app):
    app.group.create_new(Group(name="", header="", footer=""))
