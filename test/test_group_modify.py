from model.group import Group


def test_group_modify_name(app):
    app.group.modify_first(Group(name="New group"))

def test_group_modify_header(app):
    app.group.modify_first(Group(header="New group header"))

def test_group_modify_footer(app):
    app.group.modify_first(Group(footer="New group footer"))
