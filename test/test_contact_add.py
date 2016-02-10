# -*- coding: utf-8 -*-

from model.contact import Contact


def test_contact_add_new(app):
    app.contact.create_new(Contact(firstname="test", lastname="test", company="abc"))

def test_contact_add_new_empty(app):
    app.contact.create_new(Contact(firstname="", lastname="", company=""))
