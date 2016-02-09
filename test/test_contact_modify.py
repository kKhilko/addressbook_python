
from model.contact import Contact


def test_modify_firstname(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(firstname="new_firstname"))
    app.session.logout()

def test_modify_lastname(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(lastname="new_lastname"))
    app.session.logout()

def test_modify_company(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(company="new_company"))
    app.session.logout()