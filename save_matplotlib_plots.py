from generate_final_dfs_for_plot import generate
from matplotlib_plots import plot_bar_prc, plot_bar

def save_plots_with_for_loop():
    csvs_list = generate.dir_dfs
    for idx in range(len(csvs_list)):
        if len(csvs_list[idx]) == 13:
            dfs = generate.dfs_for_plot(idx)
            csv_name = csvs_list[idx]
            plot_bar_prc(dfs['mean_count_df'], 'industry', 'div_prc_mean', 'Industry', 'Dividend yield %', 'Dividend Yield by Industry', csv_name)
            plot_bar(dfs['mean_count_df'], 'industry', 'in_industry_count', 'Industry', 'Count', 'Total Number of Companies in Industry', csv_name)
            plot_bar_prc(dfs['div_sum_df'], 'industry', 'dividend_prc', 'Industry', 'SUM %', 'Total Amount of Dividend Yield in Industry', csv_name)
            plot_bar(dfs['div_sum_df'], 'industry', 'dividend_prc', 'Industry', 'SUM $', 'Total Amount of Dividends in Industry', csv_name)
            plot_bar_prc(dfs['location_df'], 'location', 'dividend_prc', 'Location', 'Dividend yield', 'Dividend Yield by Location', csv_name)

save_plots_with_for_loop()