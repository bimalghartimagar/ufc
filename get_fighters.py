import os

from db import DBUtils
from query import SELECT_FIGHTERS

from scraper import get_env_as_dict

def get_fighters():
    try:
        db_conn = DBUtils(get_env_as_dict())
        db_conn.open()

        fighters_list = db_conn.execute_query(SELECT_FIGHTERS)

        for fighter in fighters_list:
            print(fighter.get('name'))

    except Exception as e:
        db_conn.close()
    else:
        db_conn.close()


if __name__ == "__main__":
    get_fighters()