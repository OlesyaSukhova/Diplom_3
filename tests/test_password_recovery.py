import allure

from curl import forgot_password_page_url, password_recovery_confirmation_page_url
from pages.login_page import LoginPage

class TestRecoveryPassword:
    @allure.title('Успешный переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_successful_recovery_password(self, driver):
        login_page = LoginPage(driver)
        login_page.wait_for_login_page()
        login_page.click_on_button_recovery_password()
        assert login_page.is_current_url(forgot_password_page_url)

    @allure.title('Успешный ввод почты в поле Email и клик по кнопке Восстановить для перехода на страницу подтверждения изменения пароля')
    def test_click_on_recovery_button(self, driver, generate_user_data):
        login_page = LoginPage(driver)
        login_page.wait_for_forgot_password_page()
        login_page.click_on_email_field()
        login_page.enter_email(generate_user_data['email'])
        login_page.click_on_button_restore()
        assert login_page.is_current_url(password_recovery_confirmation_page_url)

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным и подсвечивает его')
    def test_click_on_show_or_hide_button(self, driver, generate_user_data):
        login_page = LoginPage(driver)
        login_page.wait_for_forgot_password_page()
        login_page.click_on_email_field()
        login_page.enter_email(generate_user_data['email'])
        login_page.click_on_button_restore()
        login_page.wait_for_overlay_to_hide()
        login_page.click_on_button_show_or_hide()
        assert login_page.is_password_active()
