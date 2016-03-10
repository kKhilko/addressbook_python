from random import randrange
import random
from model.group import Group


def test_modify_group_load_db_data(app, db):
    if db.get_group_list == 0:
        app.group.create_new(Group(name="test"))
    old_group = db.get_group_list()
    index = randrange(len(old_group))
    group = Group(name="New group")
    group.id = old_group[index].id
    app.group.modify_group_by_id(group.id, group)
    assert len(old_group) == app.group.count()
    new_group = app.group.get_list()
    old_group[index] = group
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
    ui_list = app.group.get_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


# def test_group_modify_name(app):
#     if app.group.count() == 0:
#         app.group.create_new(Group(name="test"))
#     old_group = app.group.get_list()
#     index = randrange(len(old_group))
#     group = Group(name="New group")
#     group.id = old_group[index].id
#     app.group.modify_by_index(index, group)
#     assert len(old_group) == app.group.count()
#     new_group = app.group.get_list()
#     old_group[index] = group
#     assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


# def test_group_modify_header(app):
#     if app.group.count() == 0:
#         app.group.create_new(Group(name="test"))
#     old_group = app.group.get_list()
#     index = randrange(len(old_group))
#     app.group.modify_by_index(index, Group(header="New group header"))
#     assert len(old_group) == app.group.count()
#

#
# def test_group_modify_footer(app):
#     if app.group.count() == 0:
#         app.group.create_new(Group(name="test"))
#     old_group = app.group.get_list()
#     app.group.modify_first(Group(footer="New group footer"))
#     new_group = app.group.get_list()
#     assert len(old_group) == len(new_group)
