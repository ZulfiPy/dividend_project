from generate_final_dfs_for_plot import generate
from name_generator import df_year
from clean_data import handle
import folium
from folium.plugins import MarkerCluster

class FoliumPlotter:
    def __init__(self):
        self.dfs = [df for df in generate.dir_dfs if len(df) == 13]

    def plot_folium_map(self, df_name):
        df = handle.final_df(df_name)

        m = folium.Map(location=[37.0902, -95.7129], zoom_start=5)
        marker_cluster = MarkerCluster().add_to(m)

        for i, row in df.iterrows():
            popup_content = f"Location: {row['location']}<br>Stock: {row['ticker']}<br>Dividend yield: {row['dividend_prc']}"
            folium.Marker([row['latitude'], row['longitude']], popup=popup_content).add_to(marker_cluster)

        folium_fin_path = f"/Users/zulf/Documents/GitHub/div/folium_plots_directory/folium_{df_year(df_name)}.html"
        m.save(folium_fin_path)

    def save_folium_maps(self):
        for df in self.dfs:
            self.plot_folium_map(df)

folium_plotter = FoliumPlotter()
folium_plotter.save_folium_maps()