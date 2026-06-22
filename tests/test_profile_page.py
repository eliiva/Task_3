import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from urls import login_page_url, profile_page_url, order_history_page_url

class TestProfilePage:

    @allure.title('Проверка перехода в личный кабинет')
    @allure.description('На главной кликаем на личный кабинет и проверяем, что произошёл редирект в личный кабинет')
    def test_redirect_to_profile_page(self, driver):
        driver.get(login_page_url)

        login_page = LoginPage(driver)
        login_page.login_registered_user()
        
        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.click_profile_link()

        assert main_page.wait_for_url_change_to(profile_page_url)

    @allure.title('Проверка перехода в раздел история заказов')
    @allure.description('В личном кабинете кликаем на историю заказов и проверяем, что произошёл редирект в историю заказов')
    def test_redirect_to_order_history(self, driver):
        driver.get(login_page_url)

        login_page = LoginPage(driver)
        login_page.login_registered_user()
        
        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.click_profile_link()

        profile_page = ProfilePage(driver)
        profile_page.wait_for_load_profile_page()
        profile_page.click_order_history_link()

        assert profile_page.wait_for_url_change_to(order_history_page_url)

    @allure.title('Проверка выхода из личного кабинета')
    @allure.description('В личном кабинете кликаем на выход и проверяем, что произошёл редирект на страницу логина')
    def test_exit_from_profile_page(self, driver):
        driver.get(login_page_url)

        login_page = LoginPage(driver)
        login_page.login_registered_user()
        
        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.click_profile_link()

        profile_page = ProfilePage(driver)
        profile_page.wait_for_load_profile_page()
        profile_page.click_exit_button()

        assert profile_page.wait_for_url_change_to(login_page_url)
