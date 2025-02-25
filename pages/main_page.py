import time

import allure

from curl import  login_page_url
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Дождаться загрузку главной страницы')
    def main_page_loading_wait(self):
        self.wait_for_overlay_to_hide()

    @allure.step('Дождаться скрытия оверлеев')
    def wait_for_overlay_to_hide(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY_1)

    @allure.step('Дождаться кликабельности кнопки Конструктор')
    def wait_for_constructor_button_clickable(self):
        self.wait_for_element_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликнуть по кнопке Конструктор')
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Дождаться кликабельности кнопки Лента заказов')
    def wait_for_order_feed_button_clickable(self):
        self.wait_for_element_clickable(MainPageLocators.ORDER_FEED)

    @allure.step('Кликнуть по кнопке Лента заказов')
    def click_on_order_feed_button(self):
        self.click_on_element(MainPageLocators.ORDER_FEED)

    @allure.step('Дождаться видимости Ингредиента')
    def wait_for_ingredient_visible(self):
        self.wait_for_element(MainPageLocators.INGREDIENT)

    @allure.step('Дождаться кликабельности Ингредиента')
    def wait_for_ingredient_button_clickable(self):
        self.wait_for_element_clickable(MainPageLocators.INGREDIENT)

    @allure.step('Кликнуть по ингридиенту')
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT)

    @allure.step('Дождаться кликабельности кнопки закрытия окна с деталями ингредиента')
    def wait_for_close_details_button_clickable(self):
        self.wait_for_element_clickable(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('Кликнуть по кнопке закрытия окна с деталями ингредиента')
    def click_close_details_button(self):
        self.click_on_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('Получить текст элемента')
    def get_element_text(self):
        self.get_text_on_element(MainPageLocators.DETAILS_TEXT)

    @allure.step('Добавить игредиент в корзину')
    def drag_and_drop_ingredient_into_basket(self):
        self.drag_and_drop_on_element(MainPageLocators.INGREDIENT_TO_DROP, MainPageLocators.BASKET)

    @allure.step('Получить значение каунтера')
    def get_counter_value_of_ingredient(self):
        return self.get_counter_value(MainPageLocators.COUNTER_MUST_BE_2)

    @allure.step('Дождаться кликабельности кнопки Оформить заказ')
    def wait_for_make_an_order_button_clickable(self):
        self.wait_for_element_clickable(MainPageLocators.MAKE_AN_ORDER_BUTTON)

    @allure.step('Кликнуть по кнопке Оформить заказ')
    def click_make_an_order_button(self):
        self.click_on_element(MainPageLocators.MAKE_AN_ORDER_BUTTON)

    @allure.step('Дождаться появления текста Ваш заказ начали готовить')
    def wait_for_order_in_progress_text(self):
        self.find_element(MainPageLocators.TEXT_ORDER_IN_PROGRESS)

    @allure.step('Залогиниться')
    def log_in(self, credentials):
        self.driver.get(login_page_url)
        self.wait_for_overlay_to_hide()
        self.send_keys_to_input(AccountPageLocators.FIELD_EMAIL_IN_LOGIN, credentials['email'])
        self.send_keys_to_input(AccountPageLocators.FIELD_PASSWORD_IN_LOGIN, credentials['password'])
        self.wait_for_element_clickable(AccountPageLocators.LOGIN_BUTTON)
        self.click_on_element(AccountPageLocators.LOGIN_BUTTON)
        self.wait_for_overlay_to_hide()

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self.get_text_on_element(MainPageLocators.ORDER_NUMBER_HEADER)

    @allure.step('Дождатья кликабельности кнопки закрытия окна с номером заказа')
    def wait_close_order_number_button_clickable(self):
        self.wait_for_element_clickable(MainPageLocators.CLOSE_ORDER_NUMBER_WINDOW)

    @allure.step('Кликнуть на кнопку закрытия окна с номером заказа')
    def click_on_close_order_number_button(self):
        self.click_on_element(MainPageLocators.CLOSE_ORDER_NUMBER_WINDOW)

    @allure.step('Найти номер заказа на странице')
    def find_order_in_feed_by_number(self, order_number):
        self.wait_for_element(MainPageLocators.order_in_feed_creator(order_number))
        return self.find_element(MainPageLocators.order_in_feed_creator(order_number))

    @allure.step('Найти номер заказа на странице для графы В работе')
    def find_order_in_wip_by_number(self, order_number):
        self.wait_for_element(MainPageLocators.order_in_wip_creator(order_number))
        return self.find_element(MainPageLocators.order_in_wip_creator(order_number))

    @allure.step('Найти текст Лента заказов')
    def wait_for_feed_header(self):
        self.wait_for_element(MainPageLocators.ORDER_FEED_HEADER)

    @allure.step('Дождаться кликабельности кнопки Личный кабинет')
    def wait_for_personal_account_button_clickable(self):
        self.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Кликнуть на кнопку Личный кабинет')
    def click_personal_account_button(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Дождаться кликабельности кнопки История заказов')
    def wait_for_order_history_button_clickable(self):
        self.wait_for_element_clickable(MainPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Клик на кнопку История заказов')
    def click_on_order_history_button(self):
        self.click_on_element(MainPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Получить количество всех заказов')
    def get_number_of_total_orders(self):
        total_orders = self.get_text_on_element(MainPageLocators.ORDERS_COUNTER_TOTAL)
        return int(total_orders)

    @allure.step('Получить количество заказов за сегодняшний день')
    def get_number_of_today_orders(self):
        total_orders = self.get_text_on_element(MainPageLocators.ORDERS_COUNTER_TODAY)
        return int(total_orders)

    @allure.step('Дождаться кликабельности лого Стеллар Бургер')
    def wait_for_logo_button_clickable(self):
        self.wait_for_element_clickable(MainPageLocators.LOGO_STELLAR_BURGERS)

    @allure.step('Кликнуть на лого Стеллар Бургер')
    def click_on_logo_button(self):
        self.click_on_element(MainPageLocators.LOGO_STELLAR_BURGERS)