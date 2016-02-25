# -*- coding: utf-8 -*-
from sys import maxsize

import pytest
import random
import string

from model.group import Group

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation+" "*10
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

# testdata = [Group(name="", header="", footer="")] + [
#     Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
#     for i in range(5)
# ]

testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ['', random_string("name", 10)]
    for header in ['', random_string("header", 20)]
    for footer in ['', random_string("footer", 20)]
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_group_add(app, group):
    old_group = app.group.get_list()
    app.group.create_new(group)
    assert len(old_group)+1 == app.group.count()
    new_group = app.group.get_list()
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
