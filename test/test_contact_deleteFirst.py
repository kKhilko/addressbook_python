
def test_contact_delete_first(app):
    app.session.login("admin", "secret")
    app.contact.del_first_contact()
    app.session.logout()
