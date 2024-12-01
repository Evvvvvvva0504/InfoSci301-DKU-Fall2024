from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

# Load and prepare the data
data_path = 'Data/2016_random_20000_rows.csv'
data_random = pd.read_csv(data_path)

# You would include data processing here if needed
# data_random = feature(data_random)

app = Dash(__name__)

# Age Distribution Plot
fig_age_distribution = px.histogram(
    data_random,
    x='age',
    color='voter_party_code',
    labels={'voter_party_code': 'Party Code'},
    title='Age Distribution by Party',
    opacity=0.4,
    barmode='overlay',
    nbins=50
)
fig_age_distribution.update_traces(histnorm='probability density')  # Normalize the histogram


app.layout = html.Div([
    html.H1("Voter Data Exploration Dashboard"),
    dcc.Graph(figure=fig_age_distribution),

])

if __name__ == "__main__":
    app.run_server(debug=True,port = 8080)
