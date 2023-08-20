import pandas as pd

class Handler:
    def __init__(self):
        pass

    def open_sorted_csv(self, df):
        final_path = f'/Users/zulf/Documents/GitHub/div/data/{df}.csv'
        df = pd.read_csv(final_path, index_col=[0])
        df = df.sort_values(by='dividend_prc', ascending=False).reset_index(drop=True)
        return df

    def df_min_max_threshold(self, df):
        threshold_df = df.groupby('industry').mean(numeric_only=True).sort_values(by='dividend_prc', ascending=False).reset_index()
        min_threshold = threshold_df['dividend_prc'].min()
        df = df[(df['dividend_prc'] > min_threshold) & (df['dividend_prc'] < 10)].reset_index(drop=True)
        return df

    def final_df(self, df):
        csv_df = self.open_sorted_csv(df)
        df = self.df_min_max_threshold(csv_df)
        return df

handle = Handler()