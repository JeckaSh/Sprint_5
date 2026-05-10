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

    throw_advice_button = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(THROW_ADVICE)
    )

    # проверяем, что отображется кнопка "разместить объявление"
    assert throw_advice_button.is_displayed()

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
