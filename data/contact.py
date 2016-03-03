import random
import string

from model.contact import Contact

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join(random.choice(symbols)for i in range(random.randrange(maxlen)))

testdata = [
    Contact(firstname="test_new_contact", lastname="test", company="abc"),
    Contact(firstname="", lastname="", company="")
]

# # execute 1 simple empty test and 5 tests with random data
# testdata = [Contact(firstname="", lastname="", company="")] + [
#      Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20), company=random_string("company", 20))
#      for i in range(5)
#  ]

# execute data combination for parameters (total)
# testdata = [
#     Contact(firstname=firstname, lastname=lastname, company=company)
#     for firstname in ['', random_string("firstname", 10)]
#     for lastname in ['', random_string("lastname", 10)]
#     for company in ['', random_string("company", 10)]
#]