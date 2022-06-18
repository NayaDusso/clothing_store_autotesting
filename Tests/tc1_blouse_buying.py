from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
import time 

# Ссылка на главную страницу сайта.
link = "http://automationpractice.com/index.php"

try:
    # Запускаем Веб-драйвер Selenium, открывается браузер Chrome:
    browser = webdriver.Chrome()

    # 1. Зайти на главную страницу http://automationpractice.com/index.php.
    # Метод browser.get эквивалентен GET HTTP запросу (GET "http://automationpractice.com/index.php").
    browser.get(link)

    # 2. Выбрать черную блузку и нажать кнопку "More".
    # browser.find_element_by_css_selector - метод поиска элемента в html-коде по css-селектору.
    '''
    Описание css-селектора #homefeatured [data-id-product='2'] ~ a:
    -- #homefeature - значение id элемента = homefeature;
    -- [data-id-product='2'] - поиск по значению тэга data-id-product, равном 2;
    -- ~ a - выбор соседнего с найденным выше элемента, у которого тэг = а.
    '''
    button_more = browser.find_element_by_css_selector("#homefeatured [data-id-product='2'] ~ a")
    # Таким образом, находим кнопку "More" и на неё можно кликнуть при помощи метода click().
    button_more.click()
    
    # Проверяем условие перехода на новую страницу. Ищем элемент с id = group_1.
    condition = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.ID, "group_1"))
    )

    # 3. Выбрать размер "M".
    # Инициализируем селект(выпадающий список с выбором) по id = group_1.
    select = Select(browser.find_element_by_id("group_1"))
    # Выбираем размер "М" через атрибут величины. В html-коде "М" соответствует 2.
    select.select_by_value("2")

    # 4. Нажать кнопку "Add to cart".
    # browser.find_element_by_name - метод поиска элемента в html-коде по name.
    button_submit = browser.find_element_by_name("Submit")
    button_submit.click()

    # Ждём, пока не появится всплывающее окно:
    condition = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "icon-ok"))
    )

    # 5. Нажать кнопку "Proceed to checkout"(Всплывающее окно).
    '''
    Описание css-селектора .btn.btn-default.button.button-medium:
    -- В селекторе идёт перечисление всех классов, которые указаны в данной кнопке;
    -- Предварительно убедились в том, что эти классы характеризуют только эту кнопку.
    '''
    button_proceed = browser.find_element_by_css_selector(".btn.btn-default.button.button-medium")
    # Здесь введём неявное ожидание.
    browser.implicitly_wait(5)
    button_proceed.click()

    # Проверяем условие перехода на новую страницу. Ищем элемент с id = cart_title.
    condition = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.ID, "cart_title"))
    )

    # 6. Добавить ещё одну блузку в заказ.
    button_up_quantity = browser.find_element_by_css_selector("#cart_quantity_up_2_9_0_0")
    button_up_quantity.click()

    # 7. Нажать кнопку "Proceed to checkpoint".
    # Поиск аналогичен поиску из п.5.
    button_proceed = browser.find_element_by_css_selector(".button.btn.btn-default.standard-checkout.button-medium")
    button_proceed.click()

    # Проверяем условие перехода на новую страницу. Ищем элемент с id = email_create.
    condition = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.ID, "email_create"))
    )

    # 8. Созать e-mail аккаунт.
    # Находим input при помощи id = email_create.
    input_email = browser.find_element_by_id("email_create")
    # Пишем в нём email.
    input_email.send_keys("malya@mail.com")
    # Находим кнопку создания аккаунта по id = SubmitCreate.
    button_submit_create = browser.find_element_by_id("SubmitCreate")
    button_submit_create.click()

    # Проверяем условие перехода на новую страницу. Ищем элемент с id = account-creation_form.
    condition = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.ID, "account-creation_form"))
    )
    
    # 9. Заполняем форму регистрации.
    # Находим radiobutton с выбором мужского пола при помощи id = id_gender1.
    gender_radiobutton = browser.find_element_by_id("id_gender1")
    gender_radiobutton.click()

    # Находим input с вводом имени при помощи id = customer_firstname.
    input_customer_firstname = browser.find_element_by_id("customer_firstname")
    input_customer_firstname.send_keys("Semen")

    # Находим input с вводом фамилии при помощи id = customer_lastname.
    input_customer_lastname = browser.find_element_by_id("customer_lastname")
    input_customer_lastname.send_keys("Yakovlev")

    # Находим input с вводом email при помощи id = email.
    # input_email_2 = browser.find_element_by_id("email")
    # input_email_2.send_keys("mailyakov@yahoo.com")

    # Находим input с вводом пароля при помощи id = passwd.
    input_password = browser.find_element_by_id("passwd")
    input_password.send_keys("SemenYakovleff1102")

    # Инициализируем селект(выпадающий список с выбором) даты рождения по id = days/months/years.
    select_day = Select(browser.find_element_by_id("days"))
    select_month = Select(browser.find_element_by_id("months"))
    select_year = Select(browser.find_element_by_id("years"))
    # Выбираем 17 число через атрибут величины. Выбираем февраль (value=2). Выбираем 1999 год.
    select_day.select_by_value("17")
    select_month.select_by_value("2")
    select_year.select_by_value("1999")

    # Ставим галочки в чекбоксах на получение новостных рассылок.
    # Находим первый checkbox с при помощи id = newsletter.
    newsletter_checkbox = browser.find_element_by_id("newsletter")
    newsletter_checkbox.click()
    # Находим первый checkbox с при помощи id = optin.
    optin_checkbox = browser.find_element_by_id("optin")
    optin_checkbox.click()

    # 10. Заполняем почтовую информацию.
    # Находим input с вводом имени при помощи id = firstname.
    input_firstname = browser.find_element_by_id("firstname")
    input_firstname.send_keys("Semen")

    # Находим input с вводом фамилии при помощи id = lastname.
    input_lastname = browser.find_element_by_id("lastname")
    input_lastname.send_keys("Yakovlev")

    # Находим input с вводом компании при помощи id = company.
    input_company = browser.find_element_by_id("company")
    input_company.send_keys("MyCompany")

    # Находим input с вводом адреса при помощи id = address1/2.
    input_adress1 = browser.find_element_by_id("address1")
    input_adress1.send_keys("Vvedensky st 3/2")
    input_adress2 = browser.find_element_by_id("address2")
    input_adress2.send_keys("450")

    # Находим input с вводом города при помощи id = city.
    input_city = browser.find_element_by_id("city")
    input_city.send_keys("Moscow")

    # Инициализируем селект(выпадающий список с выбором) штата по id = id_state.
    select_state = Select(browser.find_element_by_id("id_state"))
    # Выбираем Калифорнию под номером 5.
    select_state.select_by_value("5")

    # Находим input с вводом почтового кода при помощи id = postcode.
    input_postcode = browser.find_element_by_id("postcode")
    input_postcode.send_keys("00000")

    # Находим textarea с вводом прочей информации при помощи id = other.
    input_other = browser.find_element_by_id("other")
    input_other.send_keys("I'm Semen Yakovlev from California.")

    # Находим input с вводом домашнего телефона при помощи id = phone.
    input_phone = browser.find_element_by_id("phone")
    input_phone.send_keys("+7-925-221-50-08")

    # Находим input с вводом мобильного телефона при помощи id = mobile_phone.
    input_mphone = browser.find_element_by_id("mobile_phone")
    input_mphone.send_keys("+7-915-411-22-15")

    # Находим кнопку Submit по id = submitAccount.
    button_account = browser.find_element_by_id("submitAccount")
    button_account.click()

    # Проверяем условие перехода на новую страницу. Ищем кнопку с name = processAddress.
    condition = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.NAME, "processAddress"))
    )

    # 11. Подтверждаем адрес.
    # Находим кнопку по name = processAddress.
    button_processAddress = browser.find_element_by_name("processAddress")
    button_processAddress.click()

    # Проверяем условие перехода на новую страницу. Ищем кнопку с name = processCarrier.
    condition = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.NAME, "processCarrier"))
    )

    # 12. Подтверждаем способ доставку.
    # Находим кнопку по id = processCarrier.
    button_processCarrier = browser.find_element_by_name("processCarrier")
    button_processCarrier.click()

    # Находим первый checkbox с при помощи id = cgv.
    cgv_checkbox = browser.find_element_by_id("cgv")
    cgv_checkbox.click()

    # Проверяем условие перехода на новую страницу. Ищем ссылку на оплату по class = bankwire.
    condition = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "bankwire"))
    )

    # 13. Выбираем способ оплаты.
    # Ищем ссылку на оплату по карте (class = bankwire).
    a_bankwire = browser.find_element_by_class_name("bankwire")
    a_bankwire.click()

    # Проверяем условие перехода на новую страницу. Ищем ссылку по id = cart_navigation.
    condition = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.ID, "cart_navigation"))
    )

    # 14. Постверждаем заказ.
    # Ищем кнопку по селекторам.
    button_confirm = browser.find_element_by_css_selector(".button.btn.btn-default.standard-checkout.button-medium")
    button_confirm.click()

    # Проверяем условие перехода на новую страницу. Ищем ссылку по XPATH.
    final_condition = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, "//strong[text()='Your order on My Store is complete.']"))
    )

    if final_condition:
        print("TEST IS SUCCESSFUL")
    else:
        print("TEST FAILED")


    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла