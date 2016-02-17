# -*- coding: utf-8 -*-

from model.contact import Contact


def test_contact_add_new(app):
    old_contacts = app.contact.get_list()
    contact = Contact(firstname="test_new_contact", lastname="test", company="abc")
    app.contact.create_new(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_contact_add_new_empty(app):
#     old_contacts = app.contact.get_list()
#     contact = Contact(firstname="", lastname="", company="")
#     app.contact.create_new(contact)
#     new_contacts = app.contact.get_list()
#     assert len(old_contacts)+1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
