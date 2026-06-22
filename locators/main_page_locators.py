from selenium.webdriver.common.by import By

main_page_header = [By.XPATH, ".//h1[text()='Соберите бургер']"]
profile_page_link = [By.XPATH, ".//a/p[text()='Личный Кабинет']"]
order_list_page_link = [By.XPATH, ".//a/p[text()='Лента Заказов']"]
fluorescent_bun = [By.XPATH, ".//a/p[text()='Флюоресцентная булка R2-D3']"]
spicy_sause = [By.XPATH, ".//a/p[text()='Соус Spicy-X']"]
ingredient_details_modal_header = [By.XPATH, ".//div/h2[text()='Детали ингредиента']"]
modal_close_button = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close__TnseK')]"]
burger_section = [By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]"]
fluorescent_bun_counter = [By.XPATH, ".//div/ul[1]/a[2]/div/p[@class='counter_counter__num__3nue1']"]
order_number = [By.XPATH, ".//h2[contains(@class, 'text_type_digits-large')]"]
create_order_button = [By.XPATH, ".//button[text()='Оформить заказ']"]
