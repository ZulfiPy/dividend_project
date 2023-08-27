import pandas as pd

class NaNHandler:
    def __init__(self, df):
        self.nan_indices = []
        self.nan_col_indices = dict()
        self.df = df

    def find_nans(self):
        for row in range(self.df.shape[0]):
            for col in range(self.df.shape[1]):
                if pd.isna(self.df.iloc[row, col]):
                    self.nan_indices.append((row, col))
        return self.nan_indices

    def find_nan_row_col_industry(self):
        for tpl in self.nan_indices:
            if self.df.columns[tpl[1]] not in self.nan_col_indices:
                self.nan_col_indices[self.df.columns[tpl[1]]] = [tpl]
            elif self.df.columns[tpl[1]] in self.nan_col_indices:
                self.nan_col_indices[self.df.columns[tpl[1]]].append(tpl)
        return self.nan_col_indices

    def replace_nan(self):
        for key, values in self.nan_col_indices.items():
            key_mean = round(self.df[key].mean(), 2)
            self.df[key] = self.df[key].fillna(key_mean)

    def return_cleaned_df(self):
        self.find_nans()
        self.find_nan_row_col_industry()
        self.replace_nan()
        return self.df