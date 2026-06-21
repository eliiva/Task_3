import allure
from pages.login_page import LoginPage
from pages.order_list_page import OrderListPage
from pages.order_history_page import OrderHistoryPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import login_page_url, order_list_page_url

class TestOrderListPage:
    @allure.title('Проверка отображения окна с деталями заказа')
    @allure.description('Кликаем на заказ и проверяем, что отобразилось модальное окно с деталями заказа')
    def test_show_order_details_modal(self, driver):
        driver.get(order_list_page_url)

        order_list_page = OrderListPage(driver)
        order_list_page.wait_for_load_order_list_page()
        order_list_page.click_first_order_in_list()

        assert order_list_page.wait_for_load_order_details_modal()

    @allure.title('Проверка отображения заказов пользователя в ленте')
    @allure.description('Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_show_user_orders_in_order_list(self, driver):
        driver.get(login_page_url)

        LoginPage(driver).login_registered_user()
        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        new_order_number = main_page.create_order_and_return_order_number()

        main_page.click_profile_link()
        profile_page = ProfilePage(driver)
        profile_page.wait_for_load_profile_page()
        profile_page.click_order_history_link()

        order_history_page = OrderHistoryPage(driver)
        order_history_page.wait_for_load_order_history_page()

        driver.get(order_list_page_url)
        order_list_page = OrderListPage(driver)
        order_list_page.wait_for_load_order_list_page()

        assert new_order_number in order_history_page.get_orders_numbers_from_list()
        assert new_order_number in order_list_page.get_orders_numbers_from_list()

    @allure.title('Проверка увеличения общего счётчика заказов')
    @allure.description('Проверяем, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_all_orders_counter_increased(self, driver):
        driver.get(login_page_url)

        LoginPage(driver).login_registered_user()
        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.click_order_list_page_link()

        order_list_page = OrderListPage(driver)
        order_list_page.wait_for_load_order_list_page()
        first_counter = int(order_list_page.get_all_orders_counter())

        order_list_page.click_constructor_link()
        main_page.wait_for_load_main_page()
        main_page.create_order_and_return_order_number()

        main_page.click_order_list_page_link()
        order_list_page.wait_for_load_order_list_page()
        second_counter = int(order_list_page.get_all_orders_counter())

        assert second_counter == first_counter + 1

    @allure.title('Проверка увеличения дневного счётчика заказов')
    @allure.description('Проверяем, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_today_orders_counter_increased(self, driver):
        driver.get(login_page_url)

        LoginPage(driver).login_registered_user()
        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.click_order_list_page_link()

        order_list_page = OrderListPage(driver)
        order_list_page.wait_for_load_order_list_page()
        first_counter = int(order_list_page.get_today_ordesr_counter())

        order_list_page.click_constructor_link()
        main_page.wait_for_load_main_page()
        main_page.create_order_and_return_order_number()

        main_page.click_order_list_page_link()
        order_list_page.wait_for_load_order_list_page()
        second_counter = int(order_list_page.get_today_ordesr_counter())

        assert second_counter == first_counter + 1

    @allure.title('Проверка отображения номера заказа в разделе В работе')
    @allure.description('Проверяем, после оформления заказа его номер появляется в разделе В работе')
    def test_show_user_order_in_work_list(self, driver):
        driver.get(login_page_url)

        LoginPage(driver).login_registered_user()
        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        new_order_number = main_page.create_order_and_return_order_number()
        main_page.click_modal_close_button()

        main_page.click_order_list_page_link()
        order_list_page = OrderListPage(driver)
        order_list_page.wait_for_load_order_list_page()
        order_in_work = order_list_page.get_in_work_order_number(new_order_number)

        assert int(new_order_number) == int(order_in_work)
