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
    time.sleep(9)

    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла