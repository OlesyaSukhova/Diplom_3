from selenium.webdriver.common.by import By


class MainPageLocators:
    OVERLAY_1 = [By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"]
    CONSTRUCTOR_BUTTON = [By.CSS_SELECTOR, 'nav ul li:first-child a']
    ORDER_FEED = [By.CSS_SELECTOR, 'nav ul li:nth-child(2) a']
    INGREDIENT = [By.CSS_SELECTOR, 'main ul[class^=BurgerIngredients] > a:nth-child(2)']
    CLOSE_INGREDIENT_DETAILS_BUTTON = [By.CSS_SELECTOR, 'section[class^=Modal_modal_opened] button[class^=Modal_modal__close]']
    DETAILS_TEXT = [By.CSS_SELECTOR, 'section[class^=Modal_modal_opened] h2']
    INGREDIENT_TO_DROP = [By.XPATH, ".//a[contains(@href, '/ingredient/') and @draggable='true'][1]"]
    BASKET = [By.CSS_SELECTOR, 'ul[class^=BurgerConstructor_basket]']
    COUNTER = [By.CSS_SELECTOR, 'main ul[class^=BurgerIngredients] > a:nth-child(1) div[class^=counter]']
    COUNTER_MUST_BE_2 = [By.CSS_SELECTOR, 'p[class^=counter_counter]']
    MAKE_AN_ORDER_BUTTON = [By.XPATH, '//div[starts-with(@class, "BurgerConstructor_basket__container")]//button[text()="Оформить заказ"]']
    MAKE_AN_ORDER_BUTTON_NOT_LOGGED_IN = [By.XPATH, '//div[starts-with(@class, "BurgerConstructor_basket__container")]//button[text()="Войти в аккаунт"]']
    TEXT_ORDER_IN_PROGRESS = [By.CSS_SELECTOR, 'section[class^=Modal_modal_opened] div[class^=Modal_modal__textContainer] p']
    ORDER_NUMBER_HEADER = [By.CSS_SELECTOR, 'h2[class^=Modal_modal__title]']
    CLOSE_ORDER_NUMBER_WINDOW = [By.CSS_SELECTOR, 'section[class^=Modal_modal_opened] button[class^=Modal_modal__close]']
    ORDER_HISTORY_MENU_ACTIVE = [By.XPATH, '//a[contains(@class, "Account_link_active")][text()="История заказов"]']
    ORDER_FEED_HEADER = [By.XPATH, '//h1[text()="Лента заказов"]']
    PERSONAL_ACCOUNT = [By.CSS_SELECTOR, 'header nav > a']
    ORDER_HISTORY_BUTTON = [By.XPATH, '//main//nav//ul//a[text()="История заказов"]']
    ORDERS_COUNTER_TOTAL = [By.CSS_SELECTOR, 'div[class^=OrderFeed_ordersData] div:nth-child(2) p[class^=OrderFeed_number]']
    ORDERS_COUNTER_TODAY = [By.CSS_SELECTOR, 'div[class^=OrderFeed_ordersData] div:nth-child(3) p[class^=OrderFeed_number]']
    LOGO_STELLAR_BURGERS = [By.CSS_SELECTOR, 'header nav div a']

    @staticmethod
    def order_in_feed_creator(order_number):
        return [
            By.XPATH,
            f'//div[starts-with(@class, "OrderHistory_textBox")]/p[text()="#0{order_number}"]'
        ]

    @staticmethod
    def order_in_wip_creator(order_number):
        return [
            By.XPATH,
            f'//ul[contains(@class, "OrderFeed_orderListReady")]/li[text()={order_number}]'
        ]

