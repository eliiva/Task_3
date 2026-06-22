import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from urls import login_page_url, base_url, order_list_page_url

class TestBasicFunctionality:
    @allure.title('Проверка редиректа на страницу конструктора')
    @allure.description('На странице логина кликаем на Конструктор и проверяем, что произошёл редирект на страницу конструктора')
    def test_redirect_to_main_page(self, driver):
        driver.get(login_page_url)

        login_page = LoginPage(driver)
        login_page.wait_for_load_login_page()
        login_page.click_constructor_link()

        assert login_page.wait_for_url_change_to(base_url)

    @allure.title('Проверка редиректа в ленту заказов')
    @allure.description('На главной странице кликаем на Лента заказов и проверяем, что произошёл редирект в ленту заказов')
    def test_redirect_to_order_list_page(self, driver):
        driver.get(base_url)

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.click_order_list_page_link()

        assert main_page.wait_for_url_change_to(order_list_page_url)

    @allure.title('Проверка отображения модального окна ингредиента')
    @allure.description('Кликаем на ингредиент и проверяем, что отобразилось модальное окно с деталями ингредиента')
    def test_show_ingredient_details_modal(self, driver):
        driver.get(base_url)

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.click_ingredient_name()

        assert main_page.wait_for_load_ingredient_modal()

    @allure.title('Проверка закрытия модального окна ингредиента')
    @allure.description('Кликаем на крестик в модальном окне ингредиента и проверяем, что оно закрылось')
    def test_hide_ingredient_details_modal(self, driver):
        driver.get(base_url)

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.click_ingredient_name()
        main_page.wait_for_load_ingredient_modal()
        main_page.click_modal_close_button()

        assert main_page.wait_for_close_ingredient_modal()

    @allure.title('Проверка увеличения каунтера ингредиента')
    @allure.description('Добавляем ингредиент в заказ и проверяем, что увеличивается каунтер данного ингредиента')
    def test_add_ingredient_to_order_counter_increased(self, driver):
        driver.get(base_url)

        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.add_fluorescent_bun_to_order()

        assert main_page.get_fluorescent_bun_counter() == '2'

    @allure.title('Проверка что залогиненный пользователь может оформить заказ')
    @allure.description('Кликаем на кнопку Оформить заказ и проверяем, что отобразился номер заказа')
    def test_create_order_by_registered_user(self, driver):
        driver.get(login_page_url)

        login_page = LoginPage(driver)
        login_page.login_registered_user()
        
        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.add_fluorescent_bun_to_order()
        main_page.click_create_order_button()

        assert main_page.wait_for_load_order_number()
