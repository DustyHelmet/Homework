from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_208/"

def test_the_presence_of_the_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    # Check the add to cart button
    add_to_basket_button = browser.find_element_by_css_selector("button.btn-add-to-basket").click()
    # product title
    product_title = browser.find_element_by_css_selector("div.product_main>h1").text
    # check the message about adding an product to basket
    alert_inner = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.alertinner>strong"))).text
    

    assert product_title == alert_inner, "product not added to basket"
