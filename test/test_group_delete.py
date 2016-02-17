from random import randrange

from model.group import Group


def test_group_delete_any(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="test"))
    old_group = app.group.get_list()
    index = randrange(len(old_group))
    app.group.delete_group_by_index(index)
    assert len(old_group)-1 == app.group.count()
    new_group = app.group.get_list()
    old_group[index:index+1] = []
    assert old_group == new_group


