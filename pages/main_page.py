from .base_page import BasePage

# точка в импорте
# ImportError: attempted relative import with no known parent package

"""
Page Object, который связан с главной страницей интернет-магазина.
"""


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
