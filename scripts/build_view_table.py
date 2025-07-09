import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from core.sqlite_db import SQLiteDB


def create_view_df(gdp_per_capita, life_expectancy, population, geography):
    gdp_per_capita = gdp_per_capita.copy()
    life_expectancy = life_expectancy.copy()
    population = population.copy()
    geography = geography.copy()

    gdp_per_capita = gdp_per_capita.add_prefix('gdp_per_capita_')
    life_expectancy = life_expectancy.add_prefix('life_expectancy_')
    population = population.add_prefix('population_')
    geography = geography.add_prefix('geography_')

    view_df = pd.merge(gdp_per_capita, geography, how='inner', left_on='gdp_per_capita_country',
                       right_on='geography_country')
    view_df = pd.merge(view_df, life_expectancy, how='inner', left_on=['gdp_per_capita_country', 'gdp_per_capita_time'],
                       right_on=['life_expectancy_country', 'life_expectancy_time'])
    view_df = pd.merge(view_df, population, how='inner', left_on=['gdp_per_capita_country', 'gdp_per_capita_time'],
                       right_on=['population_country', 'population_time'])

    view_df = view_df[['geography_name', 'geography_world_4region', 'gdp_per_capita_time', 'gdp_per_capita_gdp_pcap',
                       'life_expectancy_lex', 'population_pop']]

    view_df.columns = ['country_name', 'continent', 'dt_year', 'gdp_per_capita', 'life_expectancy', 'population']

    return view_df


def main():
    sqlite_db = SQLiteDB('data/gapminder.db')

    gdp_per_capita = sqlite_db.query_table_to_dataframe('gdp_per_capita')
    life_expectancy = sqlite_db.query_table_to_dataframe('life_expectancy')
    population = sqlite_db.query_table_to_dataframe('population')
    geography = sqlite_db.query_table_to_dataframe('geography')

    view_df = create_view_df(gdp_per_capita, life_expectancy, population, geography)
    sqlite_db.create_table_from_dataframe('plotting', view_df)


if __name__ == '__main__':
    main()
