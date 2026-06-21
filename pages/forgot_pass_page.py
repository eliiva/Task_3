import allure
from pages.base_page import BasePage
from locators.forgot_pass_page_locators import forgot_pass_page_header, recover_pass_button, email_input

class ForgotPassPage (BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_forgot_pass_page(self):
        self.wait_for_load_element(forgot_pass_page_header)

    @allure.step('Заполняем имейл для восстановления')
    def fill_email_input(self, email):
        self.fill_input(email_input, email)

    @allure.step('Кликаем на кнопку Восстановить')
    def click_recovery_pass_button(self):
        self.click_page_element(recover_pass_button)
        