from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators.pages_locators import PageLocators
from user_specific_info.user_info import MyCredentials
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
        1. Open the browser on https://www.pujcim.to/
        2. Log in using the button 'Přihlášení'
        3. Type in the login user_specific_info: email and password (or read from a file)
        4. check that we are logged in. If not, ask about new loging.
    """

    # driver
    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url

    # open the page
    def open_base_url(self):
        self.driver.get(self.base_url)  # open the web page
        self.log.info(f'(open_base_url) Opening the desired web page ({self.base_url}).')

    # login
    def goto_login_page(self):
        login_element = self.driver.find_element(*PageLocators.LOGIN_BUTTON)
        login_element.click()
        self.log.info('(goto_login_page) Clicking on login.')

    def check_login_page(self):
        # prihlaseni_text_element = self.driver.find_element(*PageLocators.PRIHLASENI_TEXT)
        prihlaseni_text_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PageLocators.PRIHLASENI_TEXT))

        if prihlaseni_text_element.text == 'Přihlášení':
            self.log.info('The loging page is opened - OK.')
        else:
            self.log.error(' ### There was a problem with opening of the logging page.')
            self.driver.close()
            quit()

    def input_credentials(self):
        user_email = input('Enter your email used for login: ')
        user_password = input('Enter your password for this site: ')

        return user_email, user_password

    def load_credentials(self):
        try:
            login_email = MyCredentials.EMAIL
            login_password = MyCredentials.PASSWORD
        except AttributeError:
            print('There is something wrong with the login user_specific_info in user_specific_info/user_login_credentials.')
            print('Please, insert your user_specific_info now manually:')

            login_email, login_password = self.input_credentials()
        # except FileNotFoundError:
        #     print('The file user_specific_info/user_login_credentials with your user_specific_info was not found.')
        #     print('Please, insert your user_specific_info manually:')
        #
        #     login_email, login_password = self.input_credentials()

        return login_email, login_password

    def send_credentials(self, email, password):

        email_element = self.driver.find_element(*PageLocators.EMAIL_FIELD)
        email_element.clear()
        email_element.send_keys(email)

        password_element = self.driver.find_element(*PageLocators.PASSWORD_FIELD)
        password_element.send_keys(password)

        login_button = self.driver.find_element(*PageLocators.LOGIN_BUTTON_SEND_CREDENTIALS)
        login_button.click()
        self.log.info('(send_credentials) Sending the logging user_specific_info.')

    # check the login
    def check_logged_in(self):

        try:
            element_check_loggedin = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(PageLocators.USER_LOGGED_IN))
        except TimeoutException:
            return False

        else:
            if MyCredentials.USERNAME in element_check_loggedin.text:
                return True
            return False
