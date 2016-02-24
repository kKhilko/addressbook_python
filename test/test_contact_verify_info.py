import re


def test_all_fields_on_home_page(app):
    #define random contact index
    index = app.contact.get_selected_contact_index()
    # select contact by index
    contact_from_home_page = app.contact.get_list()[index]
    # select edit contact by index
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # assert data
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.email == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.allphones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return '\n'.join([contact.email, contact.email_sec, contact.email_thr])
