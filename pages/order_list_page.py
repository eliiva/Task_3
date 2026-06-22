import allure
from pages.base_page import BasePage
from locators.order_list_page_locators import order_list_page_header, first_order_in_list_block, order_details_block, order_in_list_number, all_orders_counter, today_ordesr_counter, constructor_link, order_in_work

class OrderListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_order_list_page(self):
        self.wait_for_load_element(order_list_page_header)

    @allure.step('Кликаем на первый заказ в ленте')
    def click_first_order_in_list(self):
        self.click_page_element(first_order_in_list_block)

    @allure.step('Дожидаемся отображения модального окна заказа')
    def wait_for_load_order_details_modal(self):
        return self.wait_for_load_element(order_details_block)
    
    @allure.step('Получаем номера из ленты заказов')
    def get_orders_numbers_from_list(self):
        orders_list = self.get_orders_numbers(order_in_list_number)
        orders_nums = {order.text.lstrip('0# ').strip() for order in orders_list if order.text}

        return orders_nums

    @allure.step('Получаем количество заказов за всё время')
    def get_all_orders_counter(self):
        return self.find_element(all_orders_counter).text
    
    @allure.step('Получаем количество заказов за день')
    def get_today_ordesr_counter(self):
        return self.find_element(today_ordesr_counter).text

    @allure.step('Кликаем на Конструктор в хэдере')
    def click_constructor_link(self):
        self.click_page_element(constructor_link)

    @allure.step('Получаем номер заказа в работе')
    def get_in_work_order_number(self, expected_number):
        self.wait_for_expected_value(order_in_work, expected_number)
        raw_text = self.find_element(order_in_work).text

        return raw_text.replace("\n", "").replace(" ", "")
