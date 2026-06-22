from selenium.webdriver.common.by import By

login_page_header = [By.XPATH, ".//div/h2[text()='Вход']"]
recovery_pass_button = [By.XPATH, ".//div/p/a[text()='Восстановить пароль']"]
email_input = [By.XPATH, ".//div/input[@name='name']"]
password_input = [By.XPATH, ".//div/input[@name='Пароль']"]
login_button = [By.XPATH, ".//button[text()='Войти']"]
constructor_link = [By.XPATH, ".//a/p[text()='Конструктор']"]
