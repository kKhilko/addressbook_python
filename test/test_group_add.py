# -*- coding: utf-8 -*-

from model.group import Group


def test_group_add(app, db, json_groups):
    group = json_groups
    old_group = db.get_group_list()
    app.group.create_new(group)
    new_group = db.get_group_list()
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
    ui_list = app.group.get_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
