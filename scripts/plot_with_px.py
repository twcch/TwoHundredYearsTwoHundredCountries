import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import plotly.express as px
from core.sqlite_db import SQLiteDB


def main():
    sqlite_db = SQLiteDB('data/gapminder.db')
    plotting_df = sqlite_db.query_table_to_dataframe('plotting')
    sqlite_db.close()

    fig = px.scatter(plotting_df,
                     x='gdp_per_capita',
                     y='life_expectancy',
                     animation_frame='dt_year',
                     animation_group='country_name',
                     size='population',
                     color='continent',
                     hover_name='country_name',
                     size_max=100,
                     range_x=[500, 100000],
                     range_y=[20, 90],
                     log_x=True,
                     title='Dynamic Visualization: 200 Countries, 200 Years, 4 Minutes (1800-2023)')

    fig.write_html('docs/views.html', auto_open=True)


if __name__ == '__main__':
    main()
