from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_user_registration_success(driver, url, random_email, password):
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
    driver.find_element(*PASSWORD_FIELD).send_keys(password)
    driver.find_element(*REPEAT_PASSWORD_FIELD).send_keys(password)

    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    username = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(USERNAME)
    )

    user_avatar = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(AVATAR_BUTTON)
    )

    # проверяем, что отображается аватар пользователя
    assert user_avatar.is_displayed() and username.is_displayed()


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

    error_fileds = driver.find_element(*ERROR_FIELDS)

    # проверяем, что отображается красная рамка на полях ввода
    assert error_fileds.is_displayed() and error_message.is_displayed()


def test_user_registration_with_existing_account(driver, url, test_user, password):
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
    driver.find_element(*EMAIL_FIELD).send_keys(test_user)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)
    driver.find_element(*REPEAT_PASSWORD_FIELD).send_keys(password)

    driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(ERROR_TEXT)
    )

    error_message = driver.find_element(*ERROR_TEXT)

    error_fileds = driver.find_element(*ERROR_FIELDS)

    # проверяем, что отображается красная рамка на полях ввода
    assert error_fileds.is_displayed() and error_message.is_displayed()


def test_user_log_in_success(driver, url, test_user, password):
    driver.get(url)

    driver.find_element(*AUTH_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(LOG_IN_FORM)
    )

    # авторизуем пользователя с ранее созданными данными
    driver.find_element(*EMAIL_FIELD).send_keys(test_user)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)

    driver.find_element(*LOG_IN_BUTTON).click()

    username = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(USERNAME)
    )

    user_avatar = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(AVATAR_BUTTON)
    )

    # проверяем, что отображется имя и аватар пользователя
    assert username.is_displayed() and user_avatar.is_displayed()


def test_user_log_out_success(driver, url, test_user, password):
    driver.get(url)

    driver.find_element(*AUTH_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(LOG_IN_FORM)
    )

    # авторизуем пользователя с ранее созданными данными
    driver.find_element(*EMAIL_FIELD).send_keys(test_user)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)

    driver.find_element(*LOG_IN_BUTTON).click()

    username = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(USERNAME)
    )

    user_avatar = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(AVATAR_BUTTON)
    )

    # проверяем, что отображется имя и аватар пользователя
    assert username.is_displayed() and user_avatar.is_displayed()

    driver.find_element(*LOGOUT_BUTTON).click()

    log_in_button = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(AUTH_BUTTON)
    )

    # проверям что кнопка "войти или зарегистрироваться" снова отображается
    assert log_in_button.is_displayed()
