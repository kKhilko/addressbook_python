import mysql.connector
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select id, firstname, lastname, email from addressbook where deprecated ='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, email) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, email=email))
        finally:
            cursor.close()
        return list

    def verify_address_in_group_list(self, group_id):
        db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
        try:
            contacts_in_group = []
            l = db.get_contacts_in_group(Group(id=group_id))
            for item in l:
                contacts_in_group.append(item)
            return contacts_in_group
        finally:
            pass

    def destroy(self):
        self.connection.close()