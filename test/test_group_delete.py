
def test_group_deleteFirst(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()