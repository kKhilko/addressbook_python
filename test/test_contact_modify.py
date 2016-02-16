
from model.contact import Contact


def test_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="test_new_contact"))
    old_contacts = app.contact.get_list()
    contact = Contact(firstname="new_firstname")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_lastname(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="test_new_contact"))
    old_contacts = app.contact.get_list()
    contact = Contact(lastname="new_lastname")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_company(app):
#     if app.contact.count() == 0:
#         app.contact.create_new(Contact(firstname="test_new_contact"))
#     app.contact.modify_first_contact(Contact(company="new_company"))
