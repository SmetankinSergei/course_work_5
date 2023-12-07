from threading import Thread

from src import constants
from src.app_state import AppState
from src.db_manager import DBManager
from src.site_discover import HeadHunterDiscover


class WorkSession:
    def __init__(self):
        self.__site_discover = HeadHunterDiscover(constants.COMPANIES_ID_LIST)
        self.__db_manager = DBManager(constants.TABLES_LIST)
        self.app_state = AppState.WORK

    def collect_data(self):
        self.__db_manager.update_tables(self.__site_discover)
        print('end')
