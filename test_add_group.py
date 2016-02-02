# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group
import unittest



class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_new_group(wd, Group(name="test", header="test_header", footer="test_footer"))
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_new_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_new_group(self, wd, group):
        # open group page
        self.open_group_page(wd)
        # init new group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit new group
        wd.find_element_by_name("submit").click()
        #return to group page
        self.return_to_group_page(wd)

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        #open home page
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
