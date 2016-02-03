# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_new(Group(name="test", header="test_header", footer="test_footer"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_new(Group(name="", header="", footer=""))
    app.session.logout()
