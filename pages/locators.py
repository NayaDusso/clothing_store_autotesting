from selenium.webdriver.common.by import By


class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, ".login")
    CONTACT_LINK = (By.CSS_SELECTOR, "#contact-link > a")
    BASKET_LINK = (By.CSS_SELECTOR, ".shopping_cart > a")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search_query_top")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#searchbox > button")
    HEADER_LOGO_LINK = (By.CSS_SELECTOR, "#header_logo > a")
    NEWSLETTER_INPUT  = (By.CSS_SELECTOR, "#newsletter-input")
    NEWSLETTER_SUBMIT = (By.NAME, "submitNewsletter")


class LoginPageLocators():

    EMAIL_CREATE_INPUT = (By.CSS_SELECTOR, "#email_create")
    SUBMIT_CREATE = (By.CSS_SELECTOR, "#SubmitCreate")
    EMAIL_LOGIN_INPUT = (By.CSS_SELECTOR, "#email")
    PASS_LOGIN_INPUT = (By.CSS_SELECTOR, "#passwd")
    SUBMIT_LOGIN = (By.CSS_SELECTOR, "#SubmitLogin")
    FORGOT_PASSWD = (By.CSS_SELECTOR, "#login_form:nth-child(1) a")


class ContactPageLocators():

    SELECT_SUBJECT = (By.CSS_SELECTOR, "id_contact")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    ORDER_REFERENCE = (By.CSS_SELECTOR, "#id_order")
    FILE_UPLOAD = (By.CSS_SELECTOR, "#fileUpload")
    MESSAGE_AREA = (By.CSS_SELECTOR, "#message")
    SEND_BUTTON = (By.CSS_SELECTOR, "#submitMessage")