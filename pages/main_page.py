import allure
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.main_page_locators import main_page_header, profile_page_link, order_list_page_link, fluorescent_bun, ingredient_details_modal_header, modal_close_button, burger_section, spicy_sause, fluorescent_bun_counter, order_number, create_order_button

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_main_page(self):
        self.wait_for_load_element(main_page_header)

    @allure.step('Кликаем на Личный кабинет')
    def click_profile_link(self):
        self.click_page_element(profile_page_link)

    @allure.step('Кликаем на Лента заказов')
    def click_order_list_page_link(self):
        self.click_page_element(order_list_page_link)

    @allure.step('Кликаем на булку')
    def click_ingredient_name(self):
        self.click_page_element(fluorescent_bun)

    @allure.step('Дожидаемся отображения модального окна ингредиента')
    def wait_for_load_ingredient_modal(self):
        return self.wait_for_load_element(ingredient_details_modal_header)

    @allure.step('Кликаем на крестик модального окна')
    def click_modal_close_button(self):
        self.click_page_element(modal_close_button)

    @allure.step('Ожидаем закрытия модального окна ингредиента')
    def wait_for_close_ingredient_modal(self):
        return self.wait_for_invisibility_of_element(ingredient_details_modal_header)
    
    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient_to_order(self, ingredient):
        source_element = self.find_element(ingredient)
        target_element = self.find_element(burger_section)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    @allure.step('Добавляем булку в заказ')
    def add_fluorescent_bun_to_order(self):
        self.add_ingredient_to_order(fluorescent_bun)
    
    @allure.step('Добавляем соус в заказ')
    def add_spicy_sause_to_order(self):
        self.add_ingredient_to_order(spicy_sause)

    @allure.step('Получаем каунтер флуоресцентной булки')
    def get_fluorescent_bun_counter(self):
        return self.find_element(fluorescent_bun_counter).text
    
    @allure.step('Кликаем на кнопку Оформить заказ')
    def click_create_order_button(self):
        self.click_page_element(create_order_button)
    
    @allure.step('Дожидаемся отображения номера заказа')
    def wait_for_load_order_number(self):
        return self.wait_for_load_element(order_number)

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        self.wait_for_change_element_text(order_number, '9999')

        return self.find_element(order_number).text
    
    @allure.step('Создаём заказ и возвращаем его номер')
    def create_order_and_return_order_number(self):
        self.add_fluorescent_bun_to_order()
        self.add_spicy_sause_to_order()
        self.click_create_order_button()
        self.wait_for_load_order_number()

        return self.get_order_number()
