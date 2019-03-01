import os

from bs4 import BeautifulSoup
import requests
from psycopg2 import IntegrityError

from db import DBUtils
from query import INSERT_EVENT, INSERT_FIGHTER, INSERT_RELATION

def scrape_fighters(content):
    bs_content = BeautifulSoup(content, 'html.parser')

    tables = bs_content.find_all('table', class_="odds-table")[1]

    body = tables.find('tbody')

    fighter_rows = body.find_all('tr', class_='odd')
    fighter_rows += body.find_all('tr', class_='even')

    fighter_rows = [x.find('th').string for x in fighter_rows if 'eventprop' not in x.attrs.get('class',[])]

    return fighter_rows
    
def scrape_content(content, selector):
    bs_content = BeautifulSoup(content, 'html.parser')
    return bs_content.select_one(selector).string

def fetch_response(url):

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    return response.content

def get_env_as_dict():

    return {
    'host': os.environ['DB_HOST'],
    'port': os.environ['DB_PORT'],
    'database': os.environ['DB_NAME'],
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD']
    }

def start_scraping(url):
    try:
        content = fetch_response(url)
        
        event_name = scrape_content(content, 'div.table-header>a')

        event_date = scrape_content(content, 'span.table-header-date')

        fighters = scrape_fighters(content)

        db_conn = DBUtils(get_env_as_dict())
        db_conn.open()

        event_id_list = db_conn.execute_query(INSERT_EVENT, (event_name, event_date))

        for fighter in fighters:
            fighter_id_list = db_conn.execute_query(INSERT_FIGHTER, (fighter,))

            db_conn.execute_nonquery(INSERT_RELATION, (event_id_list[0].get('id'),fighter_id_list[0].get('id')))

    except Exception as e:
        db_conn.close()
    else:
        db_conn.close()

if __name__ == "__main__":
        URL = "https://www.bestfightodds.com/events/ufc-231-holloway-vs-ortega-1584"
        start_scraping(URL)
        