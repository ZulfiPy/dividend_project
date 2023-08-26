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
        self.temp_data = None

    def create_df(self):
        self.df = pd.DataFrame(data=None, index=range(len(self.year_indexes)), columns=self.columns)
        self.df.insert(loc=0,
                       column='Year',
                       value=self.year_indexes)
        return self.df

    def fill_df(self, df_num):
        exdf = generate.dfs_for_plot(self.df_position[df_num])['mean_count_df']
        for idx in range(len(self.df.columns[1:])):
            for i in range(len(exdf)):
                if exdf.iloc[i, 0] == self.df.columns[idx + 1]:
                    self.df.iloc[df_num, idx + 1] = round(exdf.iloc[i, 1], 2)
        return self.df

    def run_create_fill(self):
        self.create_df()
        for index, value in self.df.iterrows():
            self.fill_df(index)
        return self.df

df_creator = DataFrameCreator()