import allure
from pages.login_page import LoginPage
from pages.forgot_pass_page import ForgotPassPage
from pages.reset_pass_page import ResetPassPage
from urls import login_page_url, forgot_pass_page_url, reset_pass_page_url
from helpers import generate_email

class TestPassRecover:

    @allure.title('Проверка редиректа на страницу восстановления пароля')
    @allure.description('На странице логина кликаем на Восстановить пароль и проверяем, что произошёл редирект на страницу восстановления')
    def test_redirect_to_forgot_password_page(self, driver):
        driver.get(login_page_url)

        login_page = LoginPage(driver)
        login_page.wait_for_load_login_page()
        login_page.click_recovery_pass_button()

        assert login_page.get_current_url() == forgot_pass_page_url

    @allure.title('Проверка редиректа на экран ввода пароля')
    @allure.description('На странице восстановления вводим имейл и кликаем на Восстановить и проверяем, что отобразился экран ввода пароля')
    def test_redirect_to_reset_password_page(self, driver):
        driver.get(forgot_pass_page_url)

        forgot_page = ForgotPassPage(driver)
        forgot_page.wait_for_load_forgot_pass_page()
        forgot_page.fill_email_input(generate_email())
        forgot_page.click_recovery_pass_button()

        assert forgot_page.wait_for_url_change_to(reset_pass_page_url)

    @allure.title('Проверка клика на иконку видимости пароля')
    @allure.description('На экране ввода пароля кликаем на иконку видимости и проверяем, что инпут ввода пароля стал активным')
    def test_click_to_pass_visibility_icon(self, driver):
        driver.get(forgot_pass_page_url)

        forgot_page = ForgotPassPage(driver)
        forgot_page.wait_for_load_forgot_pass_page()
        forgot_page.fill_email_input(generate_email())
        forgot_page.click_recovery_pass_button()

        reset_page = ResetPassPage(driver)
        reset_page.wait_for_load_reset_pass_page()
        reset_page.click_pass_visibility_icon()

        assert reset_page.check_new_pass_input_active()
        