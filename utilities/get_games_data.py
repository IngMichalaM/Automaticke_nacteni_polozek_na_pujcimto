import time
import pandas as pd
from pages.base_page import BasePage
from utilities.game_muster import CONTENT_MUSTER
from user_specific_info.user_info import ItemsForUpload

class GetTheGames(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        file_path_and_name = ItemsForUpload.XLS_FILE
        sheet_name = ItemsForUpload.XLS_SHEET
        df = pd.read_excel(file_path_and_name, sheet_name)
        vals = df.values
        vals_list = vals.tolist()
        self.iterator_game_values = iter(vals_list)
        self.log.info('We got all items from the excel file.')

    def next_game(self):
        try:
            current_game = next(self.iterator_game_values)

            game_name = current_game[1]
            self.log.info(f'We got the game "{game_name}".')
            age = current_game[2]
            players = current_game[3]
            duration = current_game[4]
            game_type = current_game[6]
            game_content = current_game[12]
            more_info = current_game[13]
            about = current_game[14]
            rules = current_game[15]
            some_comment = current_game[16]
            # image_name = current_game[17]
            cena_pujcovneho_na_tyden = current_game[18]
            # print(some_comment)
            time.sleep(5)

            main_category = current_game[19]
            sub_category = current_game[20]

            the_content = (CONTENT_MUSTER.format(about, rules, players, age, duration, game_type, game_content, more_info, some_comment))

            zaloha = current_game[11]

            return zaloha, game_name, the_content, cena_pujcovneho_na_tyden,  main_category, sub_category

        except StopIteration:
            print('There is nothing left on the list.')
            self.log.warning('StopIteration: End of the current list to insert on the web.')
            return []