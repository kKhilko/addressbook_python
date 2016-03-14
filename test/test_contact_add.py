# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_add_new(app, db, json_contact):
    contact = json_contact
    old_contacts = db.get_contact_list()
    print(old_contacts)
    app.contact.create_new(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    ui_list = app.contact.get_list()
    def clean(contact):
        return Contact(firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)

