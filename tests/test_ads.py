from locators import *
from tests.data import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAds:
    def test_create_ad_without_authorization(self, driver):
        driver.get(url)

        driver.find_element(*THROW_ADVICE).click()

        error_message = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ADS_ERROR_MESSAGE)
        )

        assert error_message.is_displayed()

    def test_create_ad_with_authorization(self, driver):
        driver.get(url)

        driver.find_element(*AUTH_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LOG_IN_FORM)
        )

        driver.find_element(*EMAIL_FIELD).send_keys(test_user)
        driver.find_element(*PASSWORD_FIELD).send_keys(password)

        driver.find_element(*LOG_IN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(USERNAME)
        )

        driver.find_element(*THROW_ADVICE).click()

        ads_url = "https://qa-desk.education-services.ru/create-lisiting"

        # проверяем что перешли на страницу создания объявления
        assert driver.current_url == ads_url

        driver.find_element(*AD_NAME).send_keys("Объявление")
        driver.find_element(*AD_CATEGORY_DROPDOWN_BUTTON).click()

        category_menu = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AD_DROPDOWN_MENU)
        )

        # проверяем что выпадающее меню отображается
        assert category_menu.is_displayed()

        driver.find_element(*AD_CATEGORY_SELECT).click()

        new_category = driver.find_element(*AD_CAREGORY_DEFAULT_VALUE)
        new_category_text = new_category.get_attribute("value")

        # проверяем что категория объявления изменилась
        assert new_category_text == "Хобби"

        driver.find_element(*AD_RADIO_BUTTON_NOT_ACTIVE).click()

        driver.find_element(*AD_CITY_DROPDOWN_BUTTON).click()

        city_menu = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AD_DROPDOWN_MENU)
        )

        # проверяем что выпадающее меню отображается
        assert city_menu.is_displayed()

        driver.find_element(*AD_CITY_SELECT).click()

        new_city = driver.find_element(*AD_CITY_DEFAULT_VALUE)
        new_city_text = new_city.get_attribute("value")

        # проверяем, что город изменился
        assert new_city_text == "Санкт-Петербург"

        driver.find_element(*AD_DESCRIPTION).send_keys("Описание")
        driver.find_element(*AD_PRICE).send_keys("1000")

        driver.find_element(*AD_CREATE_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(AVATAR_BUTTON)
        )

        driver.find_element(*AVATAR_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PROFILE_TITLE)
        )

        my_ad = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PROFILE_MY_AD)
        )

        # проверяем что наши объявление отображается в профиле
        assert my_ad.is_displayed()
