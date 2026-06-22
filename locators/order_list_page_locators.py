from selenium.webdriver.common.by import By

order_list_page_header = [By.XPATH, ".//h1[text()='Лента заказов']"]
first_order_in_list_block = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_list__OLh59')]/li[1]/a"]
order_details_block = [By.XPATH, ".//div[contains(@class, 'Modal_orderBox__1xWdi')]"]
order_in_list_number = [By.XPATH, ".//div/p[contains(@class, 'text_type_digits-default')]"]
all_orders_counter = [By.XPATH, ".//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]/div[2]/p[contains(@class, 'OrderFeed_number__2MbrQ')]"]
today_ordesr_counter = [By.XPATH, ".//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]/div[3]/p[contains(@class, 'OrderFeed_number__2MbrQ')]"]
constructor_link = [By.XPATH, ".//a/p[text()='Конструктор']"]
order_in_work = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li"]
