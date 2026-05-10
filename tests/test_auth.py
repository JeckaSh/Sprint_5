from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_user_registration_success(driver, url, random_email):
    driver.get(url)

    driver.find_element(*AUTH_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(LOG_IN_FORM)
    )

    driver.find_element(*NO_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(SIGN_IN_FORM)
    )

    driver.find_element(*EMAIL_FIELD).send_keys(random_email)
    driver.find_element(*PASSWORD_FIELD).send_keys("password")
    driver.find_element(*REPEAT_PASSWORD_FIELD).send_keys("password")

    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    username = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(USERNAME)
    )

    # проверяем, что отображется имя пользователя
    assert username.is_displayed()

    user_avatar = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(AVATAR_BUTTON)
    )

    # проверяем, что отображается аватар пользователя
    assert user_avatar.is_displayed()


def test_user_registration_with_invalid_email_format(driver, url, email_without_mask):
    driver.get(url)

    driver.find_element(*AUTH_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(LOG_IN_FORM)
    )

    driver.find_element(*NO_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(SIGN_IN_FORM)
    )

    driver.find_element(*EMAIL_FIELD).send_keys(email_without_mask)

    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(ERROR_TEXT)
    )

    error_message = driver.find_element(*ERROR_TEXT)

    # проверяем, что отображается сообщение об ошибке
    assert error_message.is_displayed()

    error_fileds = driver.find_element(*ERROR_FIELDS)

    # проверяем, что отображается красная рамка на полях ввода
    assert error_fileds.is_displayed()


def test_user_registration_with_existing_account(driver, url, random_email):
    driver.get(url)

    driver.find_element(*AUTH_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(LOG_IN_FORM)
    )

    driver.find_element(*NO_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(SIGN_IN_FORM)
    )

    # регистируем пользователя
    driver.find_element(*EMAIL_FIELD).send_keys(random_email)
    driver.find_element(*PASSWORD_FIELD).send_keys("password")
    driver.find_element(*REPEAT_PASSWORD_FIELD).send_keys("password")

    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    username = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(USERNAME)
    )

    user_avatar = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(AVATAR_BUTTON)
    )

    # проверяем, что отображется имя и аватар пользователя
    assert username.is_displayed()
    assert user_avatar.is_displayed()

    # выходим из созданного профиля
    driver.find_element(*LOGOUT_BUTTON).click()

    auth_button = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(AUTH_BUTTON)
    )

    # проверяем, что снова отображается кнопка "вход и регистрации"
    assert auth_button.is_displayed()

    driver.find_element(*AUTH_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(LOG_IN_FORM)
    )

    driver.find_element(*NO_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(SIGN_IN_FORM)
    )

    # пытаем повторно зарегистировать пользователя
    driver.find_element(*EMAIL_FIELD).send_keys(random_email)
    driver.find_element(*PASSWORD_FIELD).send_keys("password")
    driver.find_element(*REPEAT_PASSWORD_FIELD).send_keys("password")

    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(ERROR_TEXT)
    )

    error_message = driver.find_element(*ERROR_TEXT)

    # проверяем, что отображается сообщение об ошибке
    assert error_message.is_displayed()

    error_fileds = driver.find_element(*ERROR_FIELDS)

    # проверяем, что отображается красная рамка на полях ввода
    assert error_fileds.is_displayed()


def test_user_log_in_success(driver, url, random_email):
    driver.get(url)

    driver.find_element(*AUTH_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(LOG_IN_FORM)
    )

    driver.find_element(*NO_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(SIGN_IN_FORM)
    )

    # регистируем пользователя
    driver.find_element(*EMAIL_FIELD).send_keys(random_email)
    driver.find_element(*PASSWORD_FIELD).send_keys("password")
    driver.find_element(*REPEAT_PASSWORD_FIELD).send_keys("password")

    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    username = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(USERNAME)
    )

    user_avatar = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(AVATAR_BUTTON)
    )

    # проверяем, что отображется имя и аватар пользователя
    assert username.is_displayed()
    assert user_avatar.is_displayed()

    # выходим из созданного профиля
    driver.find_element(*LOGOUT_BUTTON).click()

    auth_button = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(AUTH_BUTTON)
    )

    # проверяем, что снова отображается кнопка "вход и регистрации"
    assert auth_button.is_displayed()

    driver.find_element(*AUTH_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(LOG_IN_FORM)
    )

    # авторизуем пользователя с ранее созданными данными
    driver.find_element(*EMAIL_FIELD).send_keys(random_email)
    driver.find_element(*PASSWORD_FIELD).send_keys("password")

    driver.find_element(*LOG_IN_BUTTON).click()

    username = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(USERNAME)
    )

    user_avatar = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(AVATAR_BUTTON)
    )

    # проверяем, что отображется имя и аватар пользователя
    assert username.is_displayed()
    assert user_avatar.is_displayed()
