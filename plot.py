from flask import Flask, render_template #this has changed
import plotly.express as px
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json

new_df = pd.read_csv("cidades-rct-2.csv")

with open('geojs-35-mun.json', encoding='iso-8859-1') as f:
  counties = json.load(f)

def create_plot():

    data = [
        px.choropleth_mapbox(new_df, geojson=counties, color='area',   width=1200, height=700,
                           locations="cidade", featureidkey="properties.name",
                           mapbox_style="carto-positron",
                           zoom=7.5, center = {"lat": -23.49, "lon": -48.412778},
                           opacity=0.5,
                           labels={'area':'Area: ', 'cidade': 'Cidade: '}
                          ) 
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    print(len(graphJSON))
    return graphJSON

app = Flask(__name__)


@app.route('/')
def index():


    bar = create_plot()
    return render_template('temp.html', plot=bar)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')