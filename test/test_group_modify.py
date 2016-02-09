from model.group import Group


def test_group_modify_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="New group"))
    app.session.logout()


def test_group_modify_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(header="New group header"))
    app.session.logout()

def test_group_modify_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(footer="New group footer"))
    app.session.logout()