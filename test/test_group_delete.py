import random
from model.group import Group


def test_group_delete_any(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_new(Group(name="test"))
    old_group = db.get_group_list()
    group = random.choice(old_group)
    app.group.delete_group_by_id(group.id)
    assert len(old_group)-1 == app.group.count()
    new_group = db.get_group_list()
    old_group.remove(group)
    assert old_group == new_group
    if check_ui:
        assert sorted(new_group, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)
    ui_list = app.group.get_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

