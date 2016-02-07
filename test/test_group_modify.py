from model.group import Group


def test_group_modify(app):
    app.session.login(username="admin", password="secret")
    app.group.create_new(Group(name="test", header="test_header", footer="test_footer"))
    app.session.logout()
