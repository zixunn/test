import csv
import matplotlib.pyplot as plt 

# from plotly.graph_objs import Scattergeo, Layout
# from plotly import offline
#import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# filename='0508 MODIS_C6_1_Global_24h.csv'
# with open(filename)as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     #print(header_row)
    
#     for index,column_header in enumerate(header_row):
#      print(index, column_header)

#     #Get latitude,longitude,brightness,bright_t31,scan,track,acq_date,acq_time,daynight
#     lats,lons,bri4s,bri5s,scans,tracks,dates,times,daynights = [],[],[],[],[],[],[],[],[]
#     for row in reader:
#         lat = str(row[0])
#         lon = str(row[1])
#         bri4 = str(row[2])
#         bri5 = str(row[10])
#         scan = str(row[3])
#         track = str(row[4])
#         date = str(row[5])
#         time = str(row[6])
#         daynight = str(row[12])
        
#         lats.append(lat)
#         lons.append(lon)
#         bri4s.append(bri4)
#         bri5s.append(bri5)
#         scans.append(scan)
#         tracks.append(track)
#         dates.append(date)
#         times.append(time)
#         daynights.append(daynight)

# print(lats)
# print(lons)
# print(bri4s)
# print(bri5s)
# print(scans)
# print(tracks)
# print(dates)
# print(times)
# print(daynights)


#format map

# data = [Scattergeo(lon=lons, lat=lats)]
# my_layout = Layout(title='世界大火地圖')

# fig = {'data': data, 'layout':my_layout}
# offline.plot(fig, filename='emptymap.html')
df = pd.read_csv('0518MODIS_C6_1_Global_24h.csv')
df['text'] = df['acq_date'].astype(str) + ',' + df['acq_time'].astype(str)+ ',' + df['daynight'].astype(str)+ ',' + df['brightness'].astype(str) + ',' + df['bright_t31'].astype(str) + ',' + df['scan'].astype(str) + ',' + df['track'].astype(str)

fig = go.Figure(data=go.Scattergeo(
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
        colorbar_title="brightness<br>0518 2022"

    )))
fig.update_layout(
        title = '世界大火地圖',
    )
fig.show()

