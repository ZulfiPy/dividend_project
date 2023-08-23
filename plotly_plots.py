from generate_final_dfs_for_plot import generate
from name_generator import df_year
from clean_data import handle
import plotly.graph_objects as go

class PlotlyPlotter:
    def __init__(self):
        self.dfs = [df for df in generate.dir_dfs if len(df) == 13]

    def plot_plotly(self, df_name):
        df = handle.final_df(df_name)
        fig = go.Figure()

        for i, row in df.iterrows():
            fig.add_trace(
                go.Scattermapbox(
                    lat=[row['latitude']],
                    lon=[row['longitude']],
                    mode='markers',
                    marker=dict(
                        size=row['dividend_prc'] * 5,
                        color=row['dividend_prc'],
                        opacity=1,
                        showscale=False
                    ),
                    text=f"Location: {row['location']}<br>Stock: {row['ticker']}<br>Dividend yield: {row['dividend_prc']}%",
                    name=row['ticker']
                )
            )

        fig.update_layout(
            mapbox_style='stamen-toner',
            mapbox_zoom=3,
            mapbox_center={'lat': df['latitude'].mean(), 'lon': df['longitude'].mean()},
            margin={'r': 0, 't': 0, 'l': 0, 'b': 0}
        )

        plotly_fin_path = f"/Users/zulf/Documents/GitHub/div/plotply_plots_directory/plotly_{df_year(df_name)}.html"

        fig.write_html(plotly_fin_path)

    def save_plotly_plots(self):
        for df in self.dfs:
            self.plot_plotly(df)


plot_plotly = PlotlyPlotter()
plot_plotly.save_plotly_plots()