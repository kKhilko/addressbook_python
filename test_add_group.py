# -*- coding: utf-8 -*-
from group import Group
import pytest
from application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="test", header="test_header", footer="test_footer"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()
