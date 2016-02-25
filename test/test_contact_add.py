# -*- coding: utf-8 -*-
import random
import string

import pytest
from model.contact import Contact

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join(random.choice(symbols)for i in range(random.randrange(maxlen)))

## execute simple 2 test scenario
# testdata = [
#     Contact(firstname="test_new_contact", lastname="test", company="abc"),
#     Contact(firstname="", lastname="", company="")
# ]

# # execute 1 simple empty test and 5 tests with random data
# testdata = [Contact(firstname="", lastname="", company="")] + [
#      Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20), company=random_string("company", 20))
#      for i in range(5)
#  ]

# execute data combination for parameters (total)
testdata = [
    Contact(firstname=firstname, lastname=lastname, company=company)
    for firstname in ['', random_string("firstname", 10)]
    for lastname in ['', random_string("lastname", 10)]
    for company in ['', random_string("company", 10)]
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_contact_add_new(app, contact):
    old_contacts = app.contact.get_list()
    app.contact.create_new(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

