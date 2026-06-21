from selenium.webdriver.common.by import By

pass_visibility_icon = [By.XPATH, ".//div[contains(.//label, 'Пароль')]/div[contains(@class, 'input__icon-action')]"]
new_pass_input_masked = [By.XPATH, ".//div[contains(.//label, 'Пароль')]//input[@type='password']"]
new_pass_input_visible = [By.XPATH, ".//div[contains(.//label, 'Пароль')]//input[@type='text']"]
