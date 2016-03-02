# -*- coding: utf-8 -*-

import pytest
from data.groups import testdata
# from data.add_group import constant as testdata

from model.group import Group


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_group_add(app, group):
    old_group = app.group.get_list()
    app.group.create_new(group)
    assert len(old_group)+1 == app.group.count()
    new_group = app.group.get_list()
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
