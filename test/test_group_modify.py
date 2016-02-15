from model.group import Group


def test_group_modify_name(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="test"))
    old_group = app.group.get_list()
    app.group.modify_first(Group(name="New group"))
    new_group = app.group.get_list()
    assert len(old_group) == len(new_group)


def test_group_modify_header(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="test"))
    old_group = app.group.get_list()
    app.group.modify_first(Group(header="New group header"))
    new_group = app.group.get_list()
    assert len(old_group) == len(new_group)

def test_group_modify_footer(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="test"))
    old_group = app.group.get_list()
    app.group.modify_first(Group(footer="New group footer"))
    new_group = app.group.get_list()
    assert len(old_group) == len(new_group)
