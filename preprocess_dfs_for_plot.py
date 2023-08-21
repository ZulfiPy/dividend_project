from clean_data import handle

class Preprocess:
    def __init__(self, df):
        self.df = handle.final_df(df)

    def df_mean_count(self):
        df = self.df.groupby('industry')['dividend_prc'].agg([('div_prc_mean', 'mean'), ('in_industry_count', 'count')]).sort_values(by='div_prc_mean', ascending=False)
        return df

    def df_div_sum(self):
        df = self.df.groupby('industry')[['dividend', 'dividend_prc']].sum().sort_values(by='dividend_prc', ascending=False)
        return df

    def df_location(self):
        df = self.df.groupby('location').mean(numeric_only=True).sort_values('dividend_prc', ascending=False).reset_index()
        return df