import random
import string
import os.path
import getopt
import sys

import jsonpickle

from model.contact import Contact


# create parametrize generator (need import getopt and sys)
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["numbers of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# analys for parametrs
n = 5
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join(random.choice(symbols)for i in range(random.randrange(maxlen)))

testdata = [Contact(firstname="", lastname="", company="")] + [
     Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20), company=random_string("company", 20))
     for i in range(5)]

# save data after generation
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# open file for record
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))