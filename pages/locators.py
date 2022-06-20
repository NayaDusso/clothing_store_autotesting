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


class AccountCreationPageLocators():

    TITLE_MALE = (By.CSS_SELECTOR, "#id_gender1")
    TITLE_FEMALE = (By.CSS_SELECTOR, "#id_gender2")
    FIRST_NAME = (By.CSS_SELECTOR, "#customer_firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#customer_lastname")
    EMAIL = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "#passwd")
    DATE_OF_BIRTH_DAY = (By.CSS_SELECTOR, "#days")
    DATE_OF_BIRTH_MONTH = (By.CSS_SELECTOR, "#months")
    DATE_OF_BIRTH_YEAR = (By.CSS_SELECTOR, "#years")
    NEWSLETTER_CHECK = (By.CSS_SELECTOR, "#newsletter")
    SPECIAL_OFFERS_CHECK = (By.CSS_SELECTOR, "#optin")
    ADDRESS_FIRST_NAME = (By.CSS_SELECTOR, "#firstname")
    ADDRESS_LAST_NAME = (By.CSS_SELECTOR, "#lastname")
    COMPANY = (By.CSS_SELECTOR, "#company")
    ADDRESS_L1 = (By.CSS_SELECTOR, "#address1")
    ADDRESS_L2 = (By.CSS_SELECTOR, "#address2")
    CITY = (By.CSS_SELECTOR, "#city")
    STATE = (By.CSS_SELECTOR, "#id_state")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postcode")
    COUNTRY = (By.CSS_SELECTOR, "#id_country")
    ADDITIONAL_INFORMATION = (By.CSS_SELECTOR, "#other")
    HOME_PHONE = (By.CSS_SELECTOR, "#phone")
    MOBILE_PHONE = (By.CSS_SELECTOR, "#phone_mobile")
    ALIAS = (By.CSS_SELECTOR, "#alias")
    SUBMIT_ACCOUNT = (By.CSS_SELECTOR, "#submitAccount")
