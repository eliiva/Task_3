import allure
from pages.base_page import BasePage
from locators.order_history_page_locators import order_history_list, order_in_list_number

class OrderHistoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_order_history_page(self):
        self.wait_for_load_element(order_history_list)

    @allure.step('Получаем номера из ленты заказов')
    def get_orders_numbers_from_list(self):
        orders_list = self.get_orders_numbers(order_in_list_number)
        orders_nums = {order.text.lstrip('0# ').strip() for order in orders_list if order.text}

        return orders_nums
