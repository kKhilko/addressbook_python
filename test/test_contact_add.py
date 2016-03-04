# -*- coding: utf-8 -*-

from model.contact import Contact


def test_contact_add_new(app, json_contact):
    contact = json_contact
    old_contacts = app.contact.get_list()
    app.contact.create_new(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

