from random import randrange
from model.contact import Contact
import random
import pytest


@pytest.mark.parametrize("modify_type", ["lastname", "firstname"])
def test_modify_contact_name(app, db, modify_type):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Contact(firstname="test_new_contact"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    if modify_type == "lastname":
        contact = Contact(lastname="new_lastname")
    if modify_type == "firstname":
        contact = Contact(firstname="new_first_db")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    ui_list = app.contact.get_list()
    def clean(contact):
        return Contact(firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)


# def test_modify_firstname(app, db):
#     if len(db.get_contact_list()) == 0:
#         app.contact.create_new(Contact(firstname="test_new_contact"))
#     old_contacts = db.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = Contact(firstname="new_first_db")
#     contact.id = old_contacts[index].id
#     app.contact.modify_contact_by_index(index, contact)
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = db.get_contact_list()
#     old_contacts[index] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create_new(Contact(firstname="test_new_contact"))
#     old_contacts = app.contact.get_list()
#     index = randrange(len(old_contacts))
#     contact = Contact(lastname="new_lastname")
#     contact.id = old_contacts[index].id
#     app.contact.modify_contact_by_index(index, contact)
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_list()
#     old_contacts[index] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



