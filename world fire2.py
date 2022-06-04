import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  





app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv('C:/Users/emily/Desktop/world2/0518MODIS_C6_1_Global_24h.csv')
df['text'] = df['acq_date'].astype(str) + ',' + df['acq_time'].astype(str)+ ',' + df['daynight'].astype(str)+ ',' + df['brightness'].astype(str) + ',' +  df['scan'].astype(str) 
# df = df.groupby(['acq_date', 'acq_time', 'latitude', 'longitude', 'daynight', 'brightness', 'scan'])[['Pct of Colonies Impacted']]
# df.reset_index(inplace=True)
print(df)

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("世界大火地圖", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_date",
                 options=[
                     {"label": "6/6/2022", "value": "6/6/2022"}],
                     # {"label": "5/29/2022", "value": "5/29/2022"},
                     # {"label": "5/30/2022", "value": "5/30/2022"},
                     # {"label": "5/31/2022", "value": "5/31/2022"},
                     # {"label": "6/1/2022", "value": "6/1/2022"},
                     # {"label": "6/2/2022", "value": "6/2/2022"},
                     # {"label": "6/3/2022", "value": "6/3/2022"},
                     # {"label": "6/4/2022", "value": "6/4/2022"}],
                 multi=False,
                 value="6/6/2022",
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_fire_map', figure={})

])

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_fire_map', component_property='figure')],
    [Input(component_id='slct_date', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The date was: {}".format(option_slctd)

    # dff = df.copy()
    # dff = dff[dff["acq_date"] == option_slctd]
    df["acq_date"]== option_slctd
    # dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    # df['scan'] = pd.to_numeric(df['scan'],errors='coerce'),
    fig = go.Figure(
    	data=go.Scattergeo(
		    lon = df['longitude'],
		    lat = df['latitude'],
		    text = df['text'],
		    mode = 'markers',
		    marker_color = df['brightness'],
		    marker = dict(
		        size = df['scan'].astype(float)*5,
		        opacity = 0.8,
		        reversescale = True,
		        autocolorscale = False,
		        symbol = 'circle',
		        line = dict(
		            width=1,
		            color='rgba(255, 255, 255)'
		        ),
		        colorscale = 'Oranges',#Reds,Inferno,Blues,Purples,Rainbow
		        cmin = 290,
		        color = df['brightness'],
		        cmax = 370,
		        colorbar_title="brightness<br>0606 2022"

    		)))
    fig.update_layout(
        title = 'world-fire-24hr',
    )

	# fig.show()
 # ------------------------------------------------------------------------------  
    #Bee example 
    # fig = px.choropleth(
    #     data_frame=dff,
    #     locationmode='COUNTRY',
    #     locations='state_code',
    #     scope="usa",
    #     color='Pct of Colonies Impacted',
    #     hover_data=['State', 'Pct of Colonies Impacted'],
    #     color_continuous_scale=px.colors.sequential.YlOrRd,
    #     labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
    #     template='plotly_dark'
    # )
# ------------------------------------------------------------------------------
    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

    return container, fig




# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)