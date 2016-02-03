# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_new(Contact(firstname="test", lastname="test", company="abc"))
    app.session.logout()

def test_add_new_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_new(Contact(firstname="", lastname="", company=""))
    app.session.logout()