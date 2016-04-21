# -*- coding: utf-8 -*-
from spyre import server

import time
import pandas as pd
import urllib2
import json

class StockExample(server.App):
    title = "IndexPlot"

    inputs = [{     "input_type":'dropdown',
                    "label": 'IndexType',
                    "options" : [ {"label": "VCI", "value":"VCI"},
                                  {"label": "TCI", "value":"TCI"},
                                  {"label": "VHI", "value":"VHI"}],
                    "variable_name": 'ticker',
                    "action_id": "plot" },
              {     "input_type":'dropdown',
                    "label": 'Region',
                    "options" : [ {"label": "Винницкая",         "value":"24"},
                                  {"label": "Волынская",         "value":"25"},
                                  {"label": "Днепропетровская",  "value":"05"},
                                  {"label": "Донецкая",          "value":"06"},
                                  {"label": "Житомирская",       "value":"27"},
                                  {"label": "Закарпатская",      "value":"23"},
                                  {"label": "Запорожская",       "value":"26"},
                                  {"label": "Ивано-Франковская", "value":"07"},
                                  {"label": "Киевская",          "value":"11"},
                                  {"label": "Кировоградская",    "value":"13"},
                                  {"label": "Луганская",         "value":"14"},
                                  {"label": "Львовская",         "value":"15"},
                                  {"label": "Николаевская",      "value":"16"},
                                  {"label": "Одесская",          "value":"17"},
                                  {"label": "Полтавская",        "value":"18"},
                                  {"label": "Ровненская",        "value":"19"},
                                  {"label": "Сумская",           "value":"21"},
                                  {"label": "Тернопольская",     "value":"22"},
                                  {"label": "Харьковская",       "value":"08"},
                                  {"label": "Херсонская",        "value":"09"},
                                  {"label": "Хмельницкая",       "value":"10"},
                                  {"label": "Черкасская",        "value":"01"},
                                  {"label": "Черниговская",      "value":"02"},
                                  {"label": "Черновецкая",       "value":"03"},
                                  {"label": "Киев",              "value":"12"},
                                  {"label": "Севастополь",       "value":"20"},
                                  {"label": "Автономная Республика Крым", "value":"04"},
                                          ],
                    "variable_name": 'num',
                    "action_id": "plot" },
                    {"input_type":'text',
                    "label": 'Year',
                    "variable_name": 'year',
                    "action_id": "plot"}]

    outputs = [{    "output_type" : "plot",
                    "output_id" : "plot",
                    "on_page_load" : True }]

    def getData(self,params):
        ticker = params['ticker']
        num = params['num']
        year = params['year']
        url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R" + format(num) +".txt"
        vhi_url = urllib2.urlopen(url)
        name = 'vhi' + time.strftime("%c") + '.csv'
        out = open(name, 'wb')
        out.write(vhi_url.read())
        out.close()
        df = pd.read_csv(name, index_col=False, header=1)
        df.columns = ['Year', 'Week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI', 'Area_VHI_LESS_15', 'Area_VHI_LESS_35']
        df = df[df[format(ticker)] > -1]
        df = df[df['Week'] < 22]
        df = df[df['Week'] > 9]
        df = df[df['Year'] == int(format(year))]
        df = df[['Week',format(ticker)]]
        return df

    def getPlot(self,params):
        df = self.getData(params)
        plt_obj = df.set_index('Week').plot()
        plt_obj.set_ylabel('Index')
        fig = plt_obj.get_figure()
        return fig

app = StockExample()
app.launch(port=9093)