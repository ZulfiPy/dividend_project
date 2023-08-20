import pandas as pd
import googlemaps
from dateutil import parser
import pandas_datareader as web
from api_keys import alpha_vantage_api_key, google_maps_api_key
from scrape_stock_list import sp500_dict

class Processes:
    def __init__(self):
        self.gmaps = googlemaps.Client(key=google_maps_api_key)
        self.dividend_dfs_by_year = {}

    def calculate_divs(self, stocks_for_check, year):
        self.dividend_df = pd.DataFrame(data=None,
                                        columns=['ticker', 'company', 'industry', 'location', 'dividend', 'dividend_prc'])
        start_point = parser.parse(f'{int(year)-1}-10-01')
        end_point = parser.parse(f'{year}-09-30')
        for stock, value in stocks_for_check.items():
            try:
                df = web.DataReader(stock, 'av-daily-adjusted',
                                    start=start_point,
                                    end=end_point,
                                    api_key=alpha_vantage_api_key).rename_axis('date').reset_index().drop(['high', 'low', 'volume'], axis=1)
                if df['dividend amount'].sum() > 0:
                    df = df[df['dividend amount'] > 0].reset_index(drop=True)
                    div = round(df['dividend amount'].sum(), 2)
                    div_prc = round((df['dividend amount'] / df['adjusted close']).sum() * 100, 2)
                    data = stock, value[0], value[1], value[2], div, div_prc
                    self.dividend_df.loc[len(self.dividend_df.index)] = data
            except ValueError:
                print(stock, 'not found')
        self.dividend_dfs_by_year[year] = self.dividen_df

    def get_geocode(self, location):
        response = self.gmaps.geocode(location)
        lat_lon = [response[0]['geometry']['location']['lat'], response[0]['geometry']['location']['lng']]
        return lat_lon

    def lat_lng_to_df(self, df):
        df['latitude'] = df['location'].apply(lambda x: self.get_geocode(x)[0])
        df['longitude'] = df['location'].apply(lambda x: self.get_geocode(x)[1])
        return df

    def save_csv(self, df, year):
        path = '/Users/zulf/Documents/GitHub/div/data/'
        final_path = f'{path}df{year}geo.csv'
        df.to_csv(final_path)

processes = Processes()

class Processor:
    def check_stocks_div(self, years):
        for year in years:
            processes.calculate_divs(sp500_dict, year)

class