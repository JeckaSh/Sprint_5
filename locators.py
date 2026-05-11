# locators

# Локаторы главной страницы
AUTH_BUTTON = ("xpath", ".//button[contains(text(), 'Вход и регистрация')]")
THROW_ADVICE = ("xpath", ".//button[contains(text(), 'Разместить объявление')]")

# Локаторы формы логина/регистрации
NO_ACCOUNT_BUTTON = ("xpath", ".//button[contains(text(), 'Нет аккаунта')]")
LOG_IN_BUTTON = ("xpath", ".//button[contains(text(), 'Войти')]")
EMAIL_FIELD = ("name", "email")
PASSWORD_FIELD = ("name", "password")
REPEAT_PASSWORD_FIELD = ("name", "submitPassword")
CREATE_ACCOUNT_BUTTON = ("xpath", ".//button[contains(text(), 'Создать аккаунт')]")
ALREADY_HAVE_ACCOUNT_BUTTON = (
    "xpath",
    ".//button[contains(text(), 'Уже есть аккаунт')]",
)

# Локаторы сообщений об ошибке при регистрации
ERROR_TEXT = ("xpath", ".//span[contains(text(), 'Ошибка')]")
ERROR_FIELDS = ("xpath", ".//div[@class = 'input_inputError__fLUP9']")

# Локаторы авторизованного пользователя
USERNAME = ("xpath", ".//h3[contains(text(), 'User.')]")
AVATAR_BUTTON = ("xpath", ".//button[@class='circleSmall']")
LOGOUT_BUTTON = ("xpath", ".//button[contains(text(), 'Выйти')]")

# Локаторы названия модальных окон
LOG_IN_FORM = (
    "xpath",
    ".//div[@class='homePage_modal__zSdUB']",
)
SIGN_IN_FORM = (
    "xpath",
    ".//h1[contains(text(), 'Зарегистрироваться')]",
)
ADS_ERROR_MESSAGE = (
    "xpath",
    ".//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]",
)

# Локаторы страницы добавления объявлений
ADS_LIST = ("xpath", ".//form[@class='createListing_shell__A5EA7']")
AD_NAME = ("name", "name")
AD_DESCRIPTION = ("xpath", ".//textarea[@placeholder='Описание товара']")
AD_PRICE = ("name", "price")

# Локаторы выбора категории объявления
AD_CAREGORY_DEFAULT_VALUE = ("name", "category")
AD_CATEGORY_DROPDOWN_BUTTON = (
    "xpath",
    ".//input[@value='Авто']/following::button[1]",
)
AD_DROPDOWN_MENU = ("xpath", ".//div[@class='dropDownMenu_options__CmHmm']")
AD_CATEGORY_SELECT = ("xpath", ".//span[contains(text(), 'Хобби')]")

# Локатор выбора состояния товара
AD_RADIO_BUTTON_NOT_ACTIVE = (
    "xpath",
    ".//div[@class = 'radioUnput_inputRegular__FbVbr']",
)
AD_RADIO_BUTTON_ACTIVE = ("xpath", ".//div[@class='radioUnput_inputActive__eC-HY']")

# Локаторы выбора города
AD_CITY_DEFAULT_VALUE = ("name", "city")
AD_CITY_DROPDOWN_BUTTON = (
    "xpath",
    ".//input[@value='Москва']/following::button[1]",
)
AD_CITY_SELECT = ("xpath", ".//span[contains(text(), 'Санкт-Петербург')]")

AD_CREATE_BUTTON = ("xpath", ".//button[contains(text(), 'Опубликовать')]")

# Локаторы страницы профиля
PROFILE_TITLE = ("xpath", ".//h1[contains(text(), 'Мой профиль')]")
PROFILE_MY_AD = ("xpath", ".//div[@*='card']")
