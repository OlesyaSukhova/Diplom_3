import allure

from curl import account_page_url, order_history_url, login_page_url
from pages.account_page import AccountPage


class TestPersonalAccount:
    @allure.title('Клик на кнопку Личный кабинет переводит на страницу личного аккаунта')
    def test_successful_click_on_personal_account_button(self, driver, generate_user_data):
        account_page = AccountPage(driver)
        account_page.log_in(generate_user_data)
        account_page.wait_for_personal_account_button_clickable()
        account_page.click_on_personal_account_button()
        assert account_page.is_current_url(account_page_url)

    @allure.title('Клик на кнопку История заказов переводит на страницу истории заказов')
    def test_successful_click_on_order_history_button(self, driver, generate_user_data):
        account_page = AccountPage(driver)
        account_page.log_in(generate_user_data)
        account_page.wait_for_personal_account_button_clickable()
        account_page.click_on_personal_account_button()
        account_page.wait_for_order_history_button_clickable()
        account_page.wait_for_overlay_to_hide()
        account_page.click_on_order_history_button()
        assert account_page.is_current_url(order_history_url)

    @allure.title('Клик на кнопку Выйти выходит из аккаунта')
    def test_successful_click_on_exit_button(self, driver, generate_user_data):
        account_page = AccountPage(driver)
        account_page.log_in(generate_user_data)
        account_page.wait_for_personal_account_button_clickable()
        account_page.click_on_personal_account_button()
        account_page.wait_for_exit_button_clickable()
        account_page.wait_for_overlay_to_hide()
        account_page.click_on_exit_button()
        assert account_page.is_current_url(login_page_url)



