from selenium.webdriver.common.by import By

class AccountPageLocators:
    OVERLAY_1 = [By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"]
    PERSONAL_ACCOUNT = [By.CSS_SELECTOR, 'header nav > a']
    FIELD_EMAIL_IN_LOGIN = [By.CSS_SELECTOR, "form fieldset:nth-child(1) input"]
    FIELD_PASSWORD_IN_LOGIN = [By.CSS_SELECTOR, "form fieldset:nth-child(2) input"]
    LOGIN_BUTTON = [By.CSS_SELECTOR, 'form > button']
    ORDER_HISTORY_BUTTON = [By.XPATH, '//main//ul//a[contains(@href, "order-history")]']
    EXIT_BUTTON = [By.XPATH, '//main//ul//button[contains(text(), "Выход")]']
