import random
import string

from model.contact import Contact
from model.group import Group

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join(random.choice(symbols)for i in range(random.randrange(maxlen)))


def test_add_contact_in_group(app, db):
    contact_name = Contact(firstname=random_string("first", 5), lastname="test", company="abc")
    group_name = app.contact.create_new_with_add_to_group(contact_name)
    contact_id = app.contact.get_contact_id_by_name(firstname=contact_name.firstname)
    group_id = app.group.find_group_by_name(group_name)
    item = db.verify_address_in_group_list(group_id)
    print (type(contact_id))
    for i in item:
        assert contact_id in i

