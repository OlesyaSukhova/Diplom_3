from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    FEED = [By.CSS_SELECTOR, 'ul[class^="OrderFeed_list"] li:first-child a']
    TEXT = [By.XPATH, '//section[starts-with(@class, "Modal_modal_opened")]//p[text() = "Cостав"]']
