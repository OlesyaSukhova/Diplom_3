from selenium.webdriver.common.by import By

class LoginPageLocators:
    RECOVERY_PASSWORD = [By.XPATH, '//a[contains(@href, "forgot-password")]']
    OVERLAY_1 = [By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"]
    EMAIL_FIELD = [By.CSS_SELECTOR, 'form fieldset[class^=Auth] input[name=name]']
    RESTORE_BUTTON = [By.CSS_SELECTOR, 'main form > button']
    PASSWORD_FIELD = [By.CSS_SELECTOR, 'form fieldset:nth-child(1) .input__container > div']
    PASSWORD_FIELD_CONTAINER = [By.CSS_SELECTOR, 'form fieldset:nth-child(1) div.input']
    FIELD_ACTIVE_CONTAINER = [By.CSS_SELECTOR, 'div.input_status_active']
    SHOW_OR_HIDE_BUTTON = [By.CSS_SELECTOR, 'form fieldset:nth-child(1) .input__container .input__icon']
