from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, company=None, id=None, homephone=None, mobilephone=None,
                 workphone=None, secondaryphone=None, allphones_from_home_page=None, allphones=None, alldata=None,
                 address=None, email=None, email_sec=None, email_thr=None):
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.company = company
        self.id = id
        self.allphones_from_home_page = allphones_from_home_page
        self.allphones = allphones
        self.alldata = alldata
        self.address = address
        self.email = email
        self.email_sec = email_sec
        self.email_thr = email_thr


    def __repr__(self):
        return "%s:%s" % (self.id, self.lastname)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               or (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               or (self.firstname is None or other.firstname is None or self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize