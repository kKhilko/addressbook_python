# -*- coding: utf-8 -*-

from model.group import Group


def test_group_add(app, json_groups):
    group = json_groups
    old_group = app.group.get_list()
    app.group.create_new(group)
    assert len(old_group)+1 == app.group.count()
    new_group = app.group.get_list()
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
