def generate_plot_name(title, df):
    words = title.split() + df.split('.csv')
    return '_'.join(words).lower()[:-4]

def df_year(df):
    words = df.split('.csv')
    return words[0][2:6]