import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.data import load_data
from core.sqlite_db import SQLiteDB


def main():
    gdp_per_capita, life_expectancy, population, geography = load_data()

    dicts = {'gdp_per_capita': gdp_per_capita,
             'life_expectancy': life_expectancy,
             'population': population,
             'geography': geography}

    sqlite_db = SQLiteDB('data/gapminder.db')
    sqlite_db.create_table_from_dataframes(dicts)
    sqlite_db.close()


if __name__ == '__main__':
    main()
