from random import randrange
import random
from model.contact import Contact


def test_contact_delete_first(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Contact(firstname="test_new_contact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.del_contact_by_id(contact.id)
    assert len(old_contacts)-1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_list(), key=Contact.id_or_max)
    ui_list = app.contact.get_list()
    def clean(contact):
        return Contact(firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)


