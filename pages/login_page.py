import allure
from pages.base_page import BasePage
from locators.login_page_locators import login_page_header, recovery_pass_button, email_input, password_input, login_button, constructor_link
from data import registered_user_data

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_login_page(self):
        self.wait_for_load_element(login_page_header)

    @allure.step('Кликаем на кнопку Восстановить пароль')
    def click_recovery_pass_button(self):
        self.click_page_element(recovery_pass_button)

    @allure.step('Логинимся зарегистрированным юзером')
    def login_registered_user(self):
        self.fill_input(email_input, registered_user_data['email'])
        self.fill_input(password_input, registered_user_data['password'])
        self.click_page_element(login_button)

    @allure.step('Кликаем на Конструктор в хэдере')
    def click_constructor_link(self):
        self.click_page_element(constructor_link)
