import allure

from pages.order_feed_page import OrderPage


class TestOrderFeed:
    @allure.title('При клике на заказ открыватся окно с деталями')
    def test_click_on_feed(self, driver):
        order_page = OrderPage(driver)
        order_page.order_feed_page_loading_wait()
        order_page.wait_for_feed_clickable()
        order_page.click_on_feed_button()
        assert order_page.wait_for_find_element





