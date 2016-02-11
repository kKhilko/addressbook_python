
from model.contact import Contact


def test_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="test_new_contact"))
    app.contact.modify_first_contact(Contact(firstname="new_firstname"))

def test_modify_lastname(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="test_new_contact"))
    app.contact.modify_first_contact(Contact(lastname="new_lastname"))

def test_modify_company(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="test_new_contact"))
    app.contact.modify_first_contact(Contact(company="new_company"))
