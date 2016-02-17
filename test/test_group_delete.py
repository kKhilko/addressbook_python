from model.group import Group


def test_group_deleteFirst(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="test"))
    old_group = app.group.get_list()
    app.group.delete_first_group()
    assert len(old_group)-1 == app.group.count()
    new_group = app.group.get_list()
    old_group[0:1] = []
    assert old_group == new_group


