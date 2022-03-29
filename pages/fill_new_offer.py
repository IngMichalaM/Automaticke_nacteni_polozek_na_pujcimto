import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.pages_locators import OfferFieldsLocators, NewOfferLocators
from pages.base_page import BasePage
from user_specific_info.user_info import ItemsForUpload


class FillNewOffer(BasePage):
    """ Fill the fields of the New offer. """

    def __init__(self, driver):
        super().__init__(driver)

    def fill_new_offer_fields(self, zaloha, game_name, the_content, cena_pujcovneho_na_tyden):

        item_name_element = self.driver.find_element(*OfferFieldsLocators.ITEM_NAME)
        item_name_element.send_keys(game_name)

        item_description_element = self.driver.find_element(*OfferFieldsLocators.ITEM_DESCRIPTION)
        item_description_element.send_keys(the_content)

        rental_deposti_element = self.driver.find_element(*OfferFieldsLocators.DEPOSIT)
        rental_deposti_element.send_keys(zaloha)

        rental_cost_element = self.driver.find_element(*OfferFieldsLocators.RENTAL_COST)
        rental_cost_element.send_keys(cena_pujcovneho_na_tyden)
        self.log.info(f'The new offer for {game_name} was filled. ')

        ddm = self.driver.find_element(*OfferFieldsLocators.DDM)
        ddm.click()

        dropdown_option = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(OfferFieldsLocators.DDM_OPTIONS))
        dropdown_option.click()

        # text area with additional info
        text_in = ItemsForUpload.USER_TEXT
        the_text_area = self.driver.find_element(*NewOfferLocators.INFORMACE_O_DOSTUPNOSTI)
        the_text_area.clear()
        time.sleep(1)
        the_text_area.send_keys(text_in)
