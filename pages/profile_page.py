import allure
from pages.base_page import BasePage
from locators.profile_page_locators import profile_page_description, order_history_link, exit_button

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_profile_page(self):
        self.wait_for_load_element(profile_page_description)

    @allure.step('Кликаем на историю заказов')
    def click_order_history_link(self):
        self.click_page_element(order_history_link)

    @allure.step('Кликаем на выход')
    def click_exit_button(self):
        self.click_page_element(exit_button)
