import time
import allure
from curl import login_page_url, forgot_password_page_url, password_recovery_confirmation_page_url
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Дождаться загрузку страницы авторизации')
    def wait_for_login_page(self):
        self.wait_for_page(login_page_url)
        self.wait_for_overlay_to_hide()
        self.wait_for_element_clickable(LoginPageLocators.RECOVERY_PASSWORD)

    @allure.step('Кликнуть по кнопке Восстановить пароль')
    def click_on_button_recovery_password(self):
        self.click_on_element(LoginPageLocators.RECOVERY_PASSWORD)

    @allure.step('Дождаться скрытия оверлеев')
    def wait_for_overlay_to_hide(self):
        self.wait_for_element_hide(LoginPageLocators.OVERLAY_1)
        time.sleep(1)  ## ff@mac

    @allure.step('Кликнуть по полю Email')
    def click_on_email_field(self):
        self.click_on_element(LoginPageLocators.EMAIL_FIELD)

    @allure.step('Заполнить поле Email')
    def enter_email(self, email):
        self.send_keys_to_input(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Кликнуть по кнопке Восстановить')
    def click_on_button_restore(self):
        self.click_on_element(LoginPageLocators.RESTORE_BUTTON)

    @allure.step('Дождаться загрузку страницы восстановления пароля')
    def wait_for_forgot_password_page(self):
        self.wait_for_page(forgot_password_page_url)
        self.wait_for_overlay_to_hide()
        self.wait_for_element_clickable(LoginPageLocators.EMAIL_FIELD)

    @allure.step('Дождаться загрузку страницы подтверждения восстановления пароля')
    def wait_for_reset_password_page(self):
        self.wait_for_page(password_recovery_confirmation_page_url)
        self.wait_for_overlay_to_hide()
        self.wait_for_element_clickable(LoginPageLocators.PASSWORD_FIELD)

    @allure.step('Кликнуть по кнопке показать/скрыть пароль в поле Пароль')
    def click_on_button_show_or_hide(self):
        self.click_on_element(LoginPageLocators.SHOW_OR_HIDE_BUTTON)

    @allure.step('Проверить активность поля Пароль')
    def is_password_active(self):
        return self.is_field_active(LoginPageLocators.PASSWORD_FIELD_CONTAINER)

    @allure.step('Проверить активность поля')
    def is_field_active(self, field_locator):
        field = self.find_element(field_locator)
        active_field = self.find_element(LoginPageLocators.FIELD_ACTIVE_CONTAINER)
        return field == active_field









