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
THROW_ADVICE_FORM = (
    "xpath",
    ".//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]",
)
