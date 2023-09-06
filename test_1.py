from testpage import OperationHelper as OH
import logging
import time
import yaml

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)
    username = data["username"]
    password = data["password"]
    username_w = data["username_w"]
    password_w = data["password_w"]


def test_step1(browser):
    logging.info("Тест 1 --------------------")
    test_page1 = OH(browser)
    test_page1.go_to_site()
    test_page1.enter_login(username_w)
    test_page1.enter_pswd(password_w)
    test_page1.click_login_button()
    assert test_page1.get_error_msg() == '401'
    time.sleep(3)

def test_step2(browser):
    logging.info("Тест 2 --------------------")
    testpage = OH(browser)
    testpage.go_to_site()
    testpage.enter_login(username)
    testpage.enter_pswd(password)
    testpage.click_login_button()
    time.sleep(3)
    assert testpage.get_profile_text() == f"Hello, {username}", "Test_2 FAIL"

def test_step3(browser):
    logging.info("Тест 3 --------------------")
    testpage = OH(browser)
    testpage.click_to_do_new_post()
    testpage.enter_title("Это название поста")
    testpage.enter_description("мой пост")
    testpage.enter_content("Текст поста")
    testpage.click_save_post_button()
    time.sleep(3)
    assert testpage.get_title_text() == "Это название поста", "Test_3 FAIL"

def test_step4(browser):
    logging.info("Тест 4 --------------------")
    testpage = OH(browser)
    testpage.click_contact_button()
    testpage.enter_name("Михаил")
    testpage.enter_email("tm10067@list.ru")
    testpage.enter_contact_content("Мой контакт")
    testpage.contact_us_save_button()
    time.sleep(3)
    assert testpage.get_alert_text() == "Form successfully submitted", "Test_4 FAIL"
