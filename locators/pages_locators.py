from selenium.webdriver.common.by import By


class PageLocators:
    """ Contains all used locators. """

    # login
    LOGIN_BUTTON = (By.XPATH, '//*[@class="login-popup-window_open"]')
    PRIHLASENI_TEXT = (By.XPATH, '//*[@class="login-box__title"]')  # login text

    EMAIL_FIELD = (By.XPATH, '//*[@id="frm-loginForm-user"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="frm-loginForm-password"]')
    LOGIN_BUTTON_SEND_CREDENTIALS = (By.XPATH, '//*[@id="frm-loginForm-login"]')

    # check login
    USER_LOGGED_IN = (By.CSS_SELECTOR, '#home > header > nav > ul > li > div > a')

    # insert new offer / vlozit novou nabidku
    INSERT_NEW_OFFER_BUTTON = (By.XPATH, '//*[@id="home"]/header/a/span')  # VLOZIT NOVOU NABIDKU


class NewOfferLocators:
    NEW_OFFER_H1_TITLE = (By.XPATH, '//*[@id="home"]/section[2]/div/div/div/h1')
    NEW_OFFER_H1_TITLE_TEXT = 'Nová nabídka'  # NOT A LOCATOR
    NEW_OFFER_H1_TITLE_CSS = (By.CSS_SELECTOR, '#home > section.new-offer > div > div > div > h1')

    SELECT_MAIN_CATEGORY_BUTTON = (By.XPATH, '//*[@id="snippet--category-selection"]/div/div/div/div/div[2]/b')
    SELECT_SUBCATEGORY_BUTTON = (By.XPATH, '//*[@id="snippet--category-selection"]/div[2]/div/div/div/div[2]/b')

    # select the proper cagegory
    # it is a <p> not select SELECT_MAIN_CATEGORY = (By.XPATH, '//*[@id="snippet--category-selection"]/div/div/div/div/div[2]/p')
    # SELECT_MAIN_CATEGORY = (By.XPATH, '//*[@id="category_0"]')



    # SELECT_MAIN_CATEGORY = (By.XPATH, '//*[@id="snippet--category-selection"]/div/div/div/div/div[3]/div/ul/li[4]') # Party tag from the drop down menu


    # # //*[@id="snippet--category-selection"]/div[2]/div/div/div/div[2]/b
    # SELECT_SUBCATEGORY = (By.XPATH, '//*[@id="snippet--category-selection"]/div[2]/div/div/div/div[3]/div/ul/li[6]')

    # select main category and subcategory by visible text (so that the category comes with the item from the excel file)
    SELECT_MAIN_CATEGORY_wText = "//li[contains(text(), '{}')]"  # BY.XPATH
    SELECT_SUBMAIN_CATEGORY_wText = "//li[contains(text(), '{}')]"  # BY.XPATH

    # SELECT_SUBCATEGORY = (By.XPATH, '//*[@id="snippet--category-selection"]/div[2]/div/div/div/div[2]/p')
    # SELECT_SUBCATEGORY = (By.XPATH, '//*[@id="category_1"]')

    CONTINUE_BUTTON = (By.XPATH, '//*[@id="submit_next"]')

    # DROP_DOWN_MENU = (By.XPATH, '//*[@id="frm-editOfferForm-prices-0-unit_id"]')
    DROP_DOWN_MENU = (By.ID, 'frm-editOfferForm-prices-0-unit_id')

    INFORMACE_O_DOSTUPNOSTI = (By.XPATH, "//*[@name='availability_info']")


class OfferFieldsLocators:
    ITEM_NAME = (By.XPATH, '//*[@id="frm-editOfferForm-name"]')
    ITEM_DESCRIPTION = (By.XPATH, '//*[@id="frm-editOfferForm-description"]')
    DEPOSIT = (By.XPATH, '//*[@id="frm-editOfferForm-advance_amount"]')  # ZALOHA
    RENTAL_COST = (By.XPATH, '//*[@id="frm-editOfferForm-prices-0-amount"]')
    DDM = (By.XPATH, '//*[@id="offer_prices"]/table/tbody/tr[2]/td[2]/div')
    DDM_OPTIONS = (By.XPATH, f"//li[contains(text(), 'týden')]")
