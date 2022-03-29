# This is a Python script to upload board games (and others) on pujcim.to

# PyCharm: Press Shift+F10 to execute it.

"""
About:
    1. Open the browser (Chrome) on https://www.pujcim.to/
    2. Log in using the button Přihlášení
    3. log in using users' user_specific_info - either load them from user_specific_info/usr_login_credentials.py or the user is
        asked to insert them
    4. Insert new offer
    5. Read the data to be inserted from an Excel file
    6. Fill the New offer using the values from the Excel file
    7. Wait till the user upload a picture and check the Offer and save it
    8. Go on with another item

29.3.22
"""

import time
import logging
from selenium import webdriver

from pages.fill_new_offer import FillNewOffer
from pages.login_page import LoginPage
from pages.new_offer import NewOffer
from utilities.get_games_data import GetTheGames
import utilities.custom_logger as cl
from pages.login_check import login_check

BASE_URL = 'https://www.pujcim.to/'

# logger
log = cl.custom_logger(logging_level=logging.INFO)
log.info('This is the info message logged from the main body.')

# driver
driver = webdriver.Chrome()

# open the page
page = LoginPage(driver, BASE_URL)
page.open_base_url()

# go to login
page.goto_login_page()

# check the loging page
page.check_login_page()

# login
page.send_credentials(*page.load_credentials())

# login check
login_check(page, log)

# go to the New offer (Nová nabídka)
offer = NewOffer(driver)

# load the game(s) from the Excel file
games_handler = GetTheGames(driver)

while True:
    # click on Nova nabidka
    offer.open_new_offer()

    # check that we are there
    offer.check_new_offer()

    # get next game
    dalsi_hra = games_handler.next_game()

    if dalsi_hra:
        current_zaloha, current_game_name, current_main_content, cena_pujcovneho_na_tyden, \
        main_category_name, sub_category_name = dalsi_hra
    else:
        # it is empty list
        print('We are done here. See you next time.')
        log.warning('End of the current list of items to upload on the web.')
        break

    print(f'Loaded name of the main category is: {main_category_name}')
    offer.select_main_category(main_category_name)

    print(f'Loaded name of the sub category is: {sub_category_name}')
    offer.select_sub_category(sub_category_name)

    offer.click_continue_button()

    fill_new_offer = FillNewOffer(driver)
    fill_new_offer.fill_new_offer_fields(current_zaloha, current_game_name, current_main_content, cena_pujcovneho_na_tyden)

    # Wait, until the user fill the missing necessities and check this Offer, then press enter and go on.
    user_input = input('Do you want to add another item as a new offer? (y/n): ')
    if user_input.lower() == 'n':
        log.info('The user pressed "n", so we are done here.')
        break

