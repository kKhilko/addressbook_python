from model.group import Group


def test_group_deleteFirst(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="test"))
    app.group.delete_first_group()
