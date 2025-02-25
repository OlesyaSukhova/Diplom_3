import allure

from curl import order_feed_page_url, login_page_url
from locators.account_page_locators import AccountPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Дождаться загрузку страницы Ленты заказов')
    def order_feed_page_loading_wait(self):
        self.wait_for_page(order_feed_page_url)

    @allure.step('Дождаться пока заказ станет кликабельным')
    def wait_for_feed_clickable(self):
        self.wait_for_element_clickable(OrderFeedPageLocators.FEED)

    @allure.step('Кликнуть по заказу')
    def click_on_feed_button(self):
        self.click_on_element(OrderFeedPageLocators.FEED)

    @allure.step('Дождаться появления текста Состав')
    def wait_for_find_element(self):
        self.find_element(OrderFeedPageLocators.TEXT)

    @allure.step('Залогиниться')
    def log_in(self, credentials):
        self.driver.get(login_page_url)
        self.send_keys_to_input(AccountPageLocators.FIELD_EMAIL_IN_LOGIN, credentials['email'])
        self.send_keys_to_input(AccountPageLocators.FIELD_PASSWORD_IN_LOGIN, credentials['password'])
        self.wait_for_element_clickable(AccountPageLocators.LOGIN_BUTTON)
        self.click_on_element(AccountPageLocators.LOGIN_BUTTON)

