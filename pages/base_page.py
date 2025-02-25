import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Подождать видимость элемента')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать кликабельность элемента')
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Дождаться загрузку страницы')
    def wait_for_page(self, page_url):
        self.driver.get(page_url)

    @allure.step('Найти элемент на странице')
    def find_element(self, locator, timeout=10):
        return self.driver.find_element(*locator)

    @allure.step('Сравнить урл')
    def is_current_url(self, url):
        return self.driver.current_url == url

    @allure.step('Добавить ингридиент в корзину')
    def drag_and_drop_on_element(self, s, t):
        draggable = self.driver.find_element(*s)
        droppable = self.driver.find_element(*t)

        drag_and_drop_script = """
              function simulateDragDrop(sourceNode, destinationNode) {
                  var event = document.createEvent('HTMLEvents');
                  event.initEvent('dragstart', true, true);
                  sourceNode.dispatchEvent(event);

                  var dropEvent = document.createEvent('HTMLEvents');
                  dropEvent.initEvent('drop', true, true);
                  destinationNode.dispatchEvent(dropEvent);

                  var dragEndEvent = document.createEvent('HTMLEvents');
                  dragEndEvent.initEvent('dragend', true, true);
                  sourceNode.dispatchEvent(dragEndEvent);
              }
              simulateDragDrop(arguments[0], arguments[1]);
          """
        self.driver.execute_script(drag_and_drop_script, draggable, droppable)

    @allure.step('Получить значение каунтера')
    def get_counter_value(self, counter_locator):
        counter = self.driver.find_element(*counter_locator)
        return int(counter.text)

