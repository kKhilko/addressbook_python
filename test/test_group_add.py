# -*- coding: utf-8 -*-

from model.group import Group


def test_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create_new(Group(name="test", header="test_header", footer="test_footer"))
    app.session.logout()

def test_group_add_empty(app):
    app.session.login(username="admin", password="secret")
    app.group.create_new(Group(name="", header="", footer=""))
    app.session.logout()
