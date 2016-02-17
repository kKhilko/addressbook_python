import time

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.complete_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def complete_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_field("firstname", contact.firstname)
        self.change_contact_field("lastname", contact.lastname)
        self.change_contact_field("company", contact.company)

    def change_contact_field(self, contact_field, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(contact_field).click()
            wd.find_element_by_name(contact_field).clear()
            wd.find_element_by_name(contact_field).send_keys(text)

    def del_first_contact(self):
        wd = self.app.wd
        self.click_HomeTab()
        self.select_first_element()
    # click Delete
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
    # confirm deleting
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_element(self):
        wd = self.app.wd
        wd.find_element_by_xpath('(//input[@name="selected[]"])[1]').click()

    def click_HomeTab(self):
        wd = self.app.wd
        if wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath('//a[@title="Sort on “Last name”"]'))>0:
            return
        wd.find_element_by_link_text('home').click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.click_HomeTab()
        self.select_first_element()
    # click Edit first elem
        wd.find_element_by_xpath('(//img[@title="Edit"])[1]').click()
    # modify fields
        self.complete_contact_form(new_contact_data)
    # click update
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.click_HomeTab()
        return len(wd.find_elements_by_xpath('//input[@name="selected[]"]'))

    contact_cache = None

    def get_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.click_HomeTab()
            self.contact_caches = []
            for element in wd.find_elements_by_xpath("//tr[@name = 'entry']"):
                lastname = element.find_element_by_xpath('//td[2]').text
                firstname = element.find_element_by_xpath('//td[3]').text
                id = element.find_element_by_name('selected[]').get_attribute('id')
                self.contact_caches.append(Contact(id=id, lastname=lastname, firstname=firstname))
        return list(self.contact_caches)
