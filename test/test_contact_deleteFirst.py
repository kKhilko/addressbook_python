from model.contact import Contact


def test_contact_delete_first(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="test_new_contact"))
    app.contact.del_first_contact()
