# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    app.login("admin", "secret")
    app.create_new_contact(Contact(firstname="test", lastname="test", company="abc"))
    app.logout()

def test_add_new_empty_contact(app):
    app.login("admin", "secret")
    app.create_new_contact(Contact(firstname="", lastname="", company=""))
    app.logout()