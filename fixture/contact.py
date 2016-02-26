import random
import re
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
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index):
        wd = self.app.wd
        self.click_HomeTab()
        self.select_element_by_index(index)
    # click Delete
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
    # confirm deleting
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_element(self):
        wd = self.app.wd
        wd.find_element_by_xpath('(//input[@name="selected[]"])[1]').click()

    def select_element_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath('//input[@name="selected[]"]')[index].click()

    def click_HomeTab(self):
        wd = self.app.wd
        if wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath("//a[contains(., 'Last name')]"))>0:
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

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.click_HomeTab()
        self.select_element_by_index(index)
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
            for row in wd.find_elements_by_name('entry'):
                cells = row.find_elements_by_tag_name('td')
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                email = cells[4].text
                allphones = cells[5].text
                self.contact_caches.append(Contact(id=id, lastname=lastname, firstname=firstname,
                                                   address=address, email=email,
                                                   allphones_from_home_page=allphones))
        return list(self.contact_caches)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        homephone = wd.find_element_by_name('home').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        secondaryphone = wd.find_element_by_name('phone2').get_attribute('value')
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email_sec = wd.find_element_by_name('email2').get_attribute('value')
        email_thr = wd.find_element_by_name('email3').get_attribute('value')

        return Contact(firstname=firstname, lastname=lastname, id=id,
                       address=address,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone,
                       email=email, email_sec=email_sec, email_thr=email_thr,
                       )

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(allphones=text,
                        homephone=homephone, workphone=workphone,
                        mobilephone=mobilephone, secondaryphone=secondaryphone)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.click_HomeTab()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.click_HomeTab()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_selected_contact_index(self):
        wd = self.app.wd
        self.click_HomeTab()
        all_contact = wd.find_elements_by_name('entry')
        index = random.randrange(len(all_contact))
        return index