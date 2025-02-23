import time

import allure

from curl import main_page_url, login_page_url
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Дождаться кликабельности кнопки Личный кабинет')
    def wait_for_personal_account_button_clickable(self):
        self.wait_for_element_clickable(AccountPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Клик на кнопку Личный кабинет')
    def click_on_personal_account_button(self):
        self.click_on_element(AccountPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Дождаться загрузку главной страницы')
    def wait_for_main_page(self):
        self.driver.get(main_page_url)

    @allure.step('Дождаться скрытия оверлеев')
    def wait_for_overlay_to_hide(self):
        self.wait_for_element_hide(AccountPageLocators.OVERLAY_1)
        time.sleep(1) ## ff@mac

    @allure.step('Залогиниться')
    def log_in(self, credentials):
        self.driver.get(login_page_url)
        self.wait_for_overlay_to_hide()
        self.send_keys_to_input(AccountPageLocators.FIELD_EMAIL_IN_LOGIN, credentials['email'])
        self.send_keys_to_input(AccountPageLocators.FIELD_PASSWORD_IN_LOGIN, credentials['password'])
        self.wait_for_element_clickable(AccountPageLocators.LOGIN_BUTTON)
        self.click_on_element(AccountPageLocators.LOGIN_BUTTON)
        self.wait_for_overlay_to_hide()

    @allure.step('Дождаться кликабельности кнопки История заказов')
    def wait_for_order_history_button_clickable(self):
        self.wait_for_element_clickable(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Клик на кнопку История заказов')
    def click_on_order_history_button(self):
        self.click_on_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Дождаться кликабельности кнопки Выйти')
    def wait_for_exit_button_clickable(self):
        self.wait_for_element_clickable(AccountPageLocators.EXIT_BUTTON)

    @allure.step('Клик на кнопку Выйти')
    def click_on_exit_button(self):
        self.click_on_element(AccountPageLocators.EXIT_BUTTON)

    @allure.step('Дождаться загрузку страницы логина')
    def wait_for_login_page(self):
        self.driver.get(login_page_url)




