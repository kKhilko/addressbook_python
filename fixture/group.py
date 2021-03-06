from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0:
            return
        wd.find_element_by_link_text("groups").click()

    def create_new(self, group):
        wd = self.app.wd
        # open group page
        self.open_group_page()
        # init new group creation
        wd.find_element_by_name("new").click()
        self.complete_group_form(group)
        # submit new group
        wd.find_element_by_name("submit").click()
        #return to group page
        self.return_to_group_page()
        self.group_cache = None

    def complete_group_form(self, group):
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        # open group page
        self.open_group_page()
        self.select_group_by_index(index)
        # click Delete btn
        wd.find_element_by_name('delete').click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        # open group page
        self.open_group_page()
        self.select_group_by_id(id)
        # click Delete btn
        wd.find_element_by_name('delete').click()
        self.return_to_group_page()
        self.group_cache = None

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def modify_by_index(self, index, new_group_data):
        wd = self.app.wd
        # open group page
        self.open_group_page()
        self.select_group_by_index(index)
        # click Edit group
        wd.find_element_by_name("edit").click()
        # complete Edit form
        self.complete_group_form(new_group_data)
        # submit Edit form
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def modify_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        # open group page
        self.open_group_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        # complete Edit form
        self.complete_group_form(new_group_data)
        # submit Edit form
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_xpath('(//input[@name="selected[]"])[1]').click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath('//input[@name="selected[]"]')[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value= "%s"]' % id).click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_xpath('//input[@name="selected[]"]'))

    group_cache = None

    def get_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_caches = []
            for element in wd.find_elements_by_xpath('//span[@class ="group"]'):
                elemText = element.text
                id = element.find_element_by_name('selected[]').get_attribute('value')
                self.group_caches.append(Group(name=elemText, id=id))
        return list(self.group_caches)


    def find_group_by_name(self, group_name):
        wd = self.app.wd
        self.open_group_page()
        selected_group = []
        for group in wd.find_elements_by_xpath('//span[@class ="group"]'):
            if group_name in group.text:
                group_id = group.find_element_by_name('selected[]').get_attribute('value')
                selected_group.append(group_id)
        return selected_group[0]
