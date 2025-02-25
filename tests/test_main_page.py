import allure

from curl import order_feed_page_url, main_page_url, ingredient_details_url
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Клик на кнопку Лента заказов переводит на список всех заказов')
    def test_click_on_button_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.wait_for_order_feed_button_clickable()
        main_page.click_on_order_feed_button()
        assert main_page.is_current_url(order_feed_page_url)

    @allure.title('Клик на кнопку Конструктор переводит на главную страницу')
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.wait_for_order_feed_button_clickable()
        main_page.click_on_order_feed_button()
        main_page.wait_for_constructor_button_clickable()
        main_page.click_on_constructor_button()
        assert main_page.is_current_url(main_page_url)

    @allure.title('Клик по ингредиенту открывает карточку деталей')
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.wait_for_ingredient_button_clickable()
        main_page.click_on_ingredient()
        assert main_page.is_current_url(ingredient_details_url)

    @allure.title('Всплывающее окно с деталями ингридиента можно закрыть кликом по крестику')
    def test_click_on_close_ingredient_details_button(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.wait_for_ingredient_button_clickable()
        main_page.click_on_ingredient()
        main_page.wait_for_close_details_button_clickable()
        main_page.click_close_details_button()
        main_page.wait_for_constructor_button_clickable()
        main_page.click_on_constructor_button()
        assert main_page.is_current_url(main_page_url)

    @allure.title('При добавлении товара в корзину увеличивается каунтер этого товара')
    def test_drag_and_drop_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.drag_and_drop_ingredient_into_basket()
        expected_counter_value = 2
        assert expected_counter_value == main_page.get_counter_value_of_ingredient()

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_make_an_order_by_login_user(self, driver, generate_user_data):
        main_page = MainPage(driver)
        main_page.log_in(generate_user_data)
        main_page.wait_for_ingredient_visible()
        main_page.drag_and_drop_ingredient_into_basket()
        main_page.wait_for_make_an_order_button_clickable()
        main_page.click_make_an_order_button()
        assert main_page.wait_for_order_in_progress_text

    @allure.title('Номер созданного заказа из истории заказов пользователя отображается и на страницы ленты заказов')
    def test_order_number_is_displayed_in_order_history_and_on_order_feed_list(self, driver, generate_user_data):
        main_page = MainPage(driver)
        main_page.log_in(generate_user_data)
        main_page.wait_for_ingredient_visible()
        main_page.drag_and_drop_ingredient_into_basket()
        main_page.wait_for_make_an_order_button_clickable()
        main_page.click_make_an_order_button()
        main_page.wait_close_order_number_button_clickable()
        main_page.wait_for_overlay_to_hide()
        order_number = main_page.get_order_number()
        main_page.click_on_close_order_number_button()
        main_page.wait_for_overlay_to_hide()
        main_page.click_on_order_feed_button()
        main_page.wait_for_feed_header()
        order_in_feed = main_page.find_order_in_feed_by_number(order_number)
        assert order_in_feed is not None
        main_page.wait_for_personal_account_button_clickable()
        main_page.click_personal_account_button()
        main_page.wait_for_order_history_button_clickable()
        main_page.wait_for_overlay_to_hide()
        main_page.click_on_order_history_button()
        order_in_history = main_page.find_order_in_feed_by_number(order_number)
        assert order_in_history is not None

    @allure.title('При создании нового заказа счетчик общего количества заказов увеличивается')
    def test_counter_of_all_orders_increases_after_new_one(self, driver, generate_user_data):
        main_page = MainPage(driver)
        main_page.log_in(generate_user_data)
        main_page.click_on_order_feed_button()
        main_page.wait_for_feed_header()
        total_before = main_page.get_number_of_total_orders()
        main_page.wait_for_logo_button_clickable()
        main_page.click_on_logo_button()
        main_page.wait_for_ingredient_visible()
        main_page.drag_and_drop_ingredient_into_basket()
        main_page.wait_for_make_an_order_button_clickable()
        main_page.click_make_an_order_button()
        main_page.wait_close_order_number_button_clickable()
        main_page.wait_for_overlay_to_hide()
        main_page.click_on_close_order_number_button()
        main_page.click_on_order_feed_button()
        main_page.wait_for_feed_header()
        total_after = main_page.get_number_of_total_orders()
        assert total_after > total_before

    @allure.title('При создании нового заказа счетчик  количества заказов за сегоднядший день увеличивается')
    def test_counter_of_today_orders_increases_after_new_one(self, driver, generate_user_data):
        main_page = MainPage(driver)
        main_page.log_in(generate_user_data)
        main_page.click_on_order_feed_button()
        main_page.wait_for_feed_header()
        today_before = main_page.get_number_of_today_orders()
        main_page.wait_for_logo_button_clickable()
        main_page.click_on_logo_button()
        main_page.wait_for_ingredient_visible()
        main_page.drag_and_drop_ingredient_into_basket()
        main_page.wait_for_make_an_order_button_clickable()
        main_page.click_make_an_order_button()
        main_page.wait_close_order_number_button_clickable()
        main_page.wait_for_overlay_to_hide()
        main_page.click_on_close_order_number_button()
        main_page.click_on_order_feed_button()
        main_page.wait_for_feed_header()
        today_after = main_page.get_number_of_total_orders()
        assert today_after > today_before

    @allure.title('При создании заказа его номер отображается в графе В работе')
    def test_new_order_appears_in_the_graph_in_progress(self, driver, generate_user_data):
        main_page = MainPage(driver)
        main_page.log_in(generate_user_data)
        main_page.wait_for_ingredient_visible()
        main_page.drag_and_drop_ingredient_into_basket()
        main_page.wait_for_make_an_order_button_clickable()
        main_page.click_make_an_order_button()
        main_page.wait_close_order_number_button_clickable()
        main_page.wait_for_overlay_to_hide()
        order_number = main_page.get_order_number()
        main_page.click_on_close_order_number_button()
        main_page.click_on_order_feed_button()
        main_page.wait_for_feed_header()
        order_in_wip = main_page.find_order_in_wip_by_number(order_number)
        assert order_in_wip is not None



















