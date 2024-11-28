from dash import Dash, dcc, html
import geopandas as gpd
import pandas as pd
import plotly.express as px

# Load and process data
data_path = 'Data/2016_random_20000_rows.csv'
data_random = pd.read_csv(data_path)
party_counts = data_random.groupby(['county_desc', 'voter_party_code']).size().unstack(fill_value=0)
party_counts['Dominant Party'] = party_counts.idxmax(axis=1)
party_counts = party_counts.reset_index()
party_counts['county_desc'] = party_counts['county_desc'].str.strip().str.upper()
party_mapping = {'REP': 'Republican', 'DEM': 'Democrat', 'UNA': 'Unaffiliated'}
party_counts['Dominant Party'] = party_counts['Dominant Party'].map(party_mapping).fillna('No Data')

geojson_path = "Data/NCDOT_County_Boundaries.geojson"
counties = gpd.read_file(geojson_path)
counties["CountyName"] = counties["CountyName"].str.strip().str.upper()
counties = counties.merge(party_counts[['county_desc', 'Dominant Party']], left_on='CountyName', right_on='county_desc', how='left')
counties['Dominant Party'] = counties['Dominant Party'].fillna('No Data')

# Convert GeoDataFrame to GeoJSON for Plotly
counties_json = counties.geometry.__geo_interface__

# Create a map using Plotly
fig = px.choropleth_mapbox(
    counties,
    geojson=counties_json,
    locations=counties.index,
    color="Dominant Party",
    hover_name="CountyName",
    hover_data={"Dominant Party": True},
    color_discrete_map={'Republican': 'red', 'Democrat': 'blue', 'Unaffiliated': 'gray', 'No Data': 'lightgray'},
    mapbox_style="carto-positron",
    zoom=5,
    center={"lat": 35.5, "lon": -80},
    opacity=0.5,
    labels={'Dominant Party': 'Dominant Party'}
)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, title="Party Preference by County in North Carolina", showlegend=True)

# Setup Dash app
app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1("Party Preference by County in North Carolina"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
