import mysql.connector


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)


    def get_group_list(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("")
        finally:
            cursor.close()


    def destroy(self):
        self.connection.close()