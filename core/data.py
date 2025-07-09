import pandas as pd
from pathlib import Path

DATA_PATH = Path('data')


def load_data():
    gdp_per_capita = pd.read_csv(DATA_PATH / 'ddf--datapoints--gdp_pcap--by--country--time.csv')
    life_expectancy = pd.read_csv(DATA_PATH / 'ddf--datapoints--lex--by--country--time.csv')
    population = pd.read_csv(DATA_PATH / 'ddf--datapoints--pop--by--country--time.csv')
    geography = pd.read_csv(DATA_PATH / 'ddf--entities--geo--country.csv')

    return gdp_per_capita, life_expectancy, population, geography
