from preprocess_dfs import Preprocess
import os

class Generator:
    def __init__(self):
        dir_path = '/Users/zulf/Documents/GitHub/div/data'
        self.dir_dfs = os.listdir(dir_path)

    def dfs_for_plot(self, df_num):
        mean_count_df = Preprocess(self.dir_dfs[df_num]).df_mean_count()
        div_sum_df = Preprocess(self.dir_dfs[df_num]).df_div_sum()
        location_df = Preprocess(self.dir_dfs[df_num]).df_location()[:10]

        return {
            'mean_count_df': mean_count_df,
            'div_sum_df': div_sum_df,
            'location_df': location_df
        }

generate = Generator()