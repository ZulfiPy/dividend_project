from generate_final_dfs_for_plot import generate
from name_generator import df_year
import pandas as pd


class DataFrameCreator:
    def __init__(self):
        csv_names = generate.dir_dfs
        self.df_position = [idx for idx in range(len(csv_names)) if len(csv_names[idx]) == 13]
        self.year_indexes = sorted([df_year(csv_name) for csv_name in csv_names if len(csv_name) == 13])
        self.columns = [column for column in generate.dfs_for_plot(0)['mean_count_df']['industry']]

        self.df = None

    def create_df(self):
        self.df = pd.DataFrame(data=None, index=range(len(self.year_indexes)), columns=self.columns)
        self.df.insert(loc=0,
                       column='Year',
                       value=self.year_indexes)
        return self.df

df_creator = DataFrameCreator()