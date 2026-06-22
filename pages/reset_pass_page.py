import allure
from pages.base_page import BasePage
from locators.reset_pass_page_locators import pass_visibility_icon, new_pass_input_masked, new_pass_input_visible

class ResetPassPage (BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_reset_pass_page(self):
        self.wait_for_load_element(pass_visibility_icon)

    @allure.step('Кликаем на иконку видимости пароля')
    def click_pass_visibility_icon(self):
        self.click_page_element(pass_visibility_icon)

    @allure.step('Проверяем, что поле ввода пароля не активно')
    def check_new_pass_input_inactive(self):
        return self.wait_for_load_element(new_pass_input_masked)

    @allure.step('Проверяем, что поле ввода пароля активно')
    def check_new_pass_input_active(self):
        return self.wait_for_load_element(new_pass_input_visible)
