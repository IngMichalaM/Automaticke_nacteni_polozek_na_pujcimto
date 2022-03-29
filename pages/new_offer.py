from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.pages_locators import PageLocators, NewOfferLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class NewOffer(BasePage):
    """ Handle New offer page
        Methods:
            open new offer
            check new offer
            select main category
            select subcategory
            click the button to continue
    """

    def __init__(self, driver):
        super().__init__(driver)

    def open_new_offer(self):
        element = self.driver.find_element(*PageLocators.INSERT_NEW_OFFER_BUTTON)
        element.click()
        self.log.info('(open_new_offer) Opening a new offer.')

    def check_new_offer(self):
        element = self.driver.find_element(*NewOfferLocators.NEW_OFFER_H1_TITLE)

        if element.text == NewOfferLocators.NEW_OFFER_H1_TITLE_TEXT:
            self.log.info('(check_new_offer) We are on the page with the new empty offer.')
        else:
            self.log.info('### (check_new_offer) There was a problem with the page with the new empty offer.')
            self.driver.close()
            raise ValueError('There was a problem with the New Offer.')

    def select_main_category(self, main_cat_tag: str):
        # # wait for dropdown to exist
        # SELECT_MAIN_CATEGORY_BUTTON = (By.XPATH, '//*[@id="snippet--category-selection"]/div/div/div/div/div[2]/b')
        # main_cat_ddm = WebDriverWait(self.driver, 15).until(
        #         EC.presence_of_element_located(SELECT_MAIN_CATEGORY_BUTTON))

        main_cat_ddm = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(NewOfferLocators.SELECT_MAIN_CATEGORY_BUTTON))

        main_cat_ddm.click()

        # dropdown_option = WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located((By.XPATH, f"//li[contains(text(), '{main_cat_tag}')]")))
        dropdown_option = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, NewOfferLocators.SELECT_MAIN_CATEGORY_wText.format(main_cat_tag))))
        dropdown_option.click()

    def select_sub_category(self, sub_cat_tag):

        # opens the drop down menu
        sub_cat_ddm = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(NewOfferLocators.SELECT_SUBCATEGORY_BUTTON))
        sub_cat_ddm.click()

        # dropdown_option = WebDriverWait(self.driver, 15).until(
        #        EC.presence_of_element_located((By.XPATH, f"//li[contains(text(), '{sub_cat_tag}')]")))
        dropdown_option = WebDriverWait(self.driver, 15).until(
               EC.presence_of_element_located((By.XPATH, NewOfferLocators.SELECT_SUBMAIN_CATEGORY_wText.format(sub_cat_tag))))
        dropdown_option.click()

    def click_continue_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(NewOfferLocators.CONTINUE_BUTTON)).click()


