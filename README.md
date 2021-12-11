# Автоматизация тестирования с помощью Selenium и Python
В этом модуле мы создали с нуля полноценный тестовый проект, который является финальным заданием. 

Тестирование сайта: http://selenium1py.pythonanywhere.com

### Содержание репозитория:

base_page.py — class BasePage — методы, которые применяются ко всему проекту.

main_page.py — class MainPage — наследник класса BasePage — методы взаимодействия с главной страницей. 

login_page.py — class LoginPage — наследник класса BasePage — методы взаимодействия с Login страницей.

basket_page.py - class BasketPage  — наследник класса BasePage — методы взаимодействия со страницей корзины.

product_page.py — class ProductPage — наследник класса BasePage — методы взаимодействия со страницей товара.

locators.py — локаторы, в виде констант. Для каждой страницы свой класс с локаторами.

Всё завернуто в классы, чтобы было удобно импортировать.

### Тесты:

conftest.py — конфигурация тестов — для хранения часто употребимых фикстур и хранения глобальных настроек.

test_main_page.py - тесты взаимодействия с главной страницей.

test_product_page - тест добавления товара в корзину, проверка соответствия названия и цены.


### Команда для запуска финальной проверки:
pytest -v --tb=line --language=en -m need_review test_product_page.py

#### Ожидаемый результат:
12 passed, 8 deselected, 1 xfailed
