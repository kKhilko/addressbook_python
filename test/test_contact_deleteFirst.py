from model.contact import Contact


def test_contact_delete_first(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="test_new_contact"))
    old_contacts = app.contact.get_list()
    app.contact.del_first_contact()
    new_contacts = app.contact.get_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
