import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumIosConfig:
    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self):
        des_cap = {
            "app" : "bs://7647a37db4740bb456d32340690bd253b0135249",
            "deviceName": "iPhone 11 Pro",
            "platformVersion": "13",
            "bstack:options": {
                "userName": "tobimylan_1pFN9B",
                "accessKey": "xYxViSzMdVNFtoqV4zFi",
                "projectName": "First Python project",
                "buildName": "browserstack-build-1-ios",
                "sessionName": "BStack first_test-ios"
            }
        }

        self.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAssignment(AppiumIosConfig):
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.ID, "test-Username").send_keys("John")
        self.driver.find_element(AppiumBy.ID, "test-Password").send_keys("john123")

        self.driver.find_element(AppiumBy.ID, "test-LOGIN").click()

        actual_text = self.driver.find_element(AppiumBy.XPATH,
                                               "//XCUIElementTypeStaticText[contains(@name,'Username and password')]").get_attribute(
            "name")
        print(actual_text)

        assert_that('Username and password do not match any user in this service.').is_equal_to(actual_text)

    def test_add_to_cart(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()