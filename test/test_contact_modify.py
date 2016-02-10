
from model.contact import Contact


def test_modify_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="new_firstname"))

def test_modify_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="new_lastname"))

def test_modify_company(app):
    app.contact.modify_first_contact(Contact(company="new_company"))
