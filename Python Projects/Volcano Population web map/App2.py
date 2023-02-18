import folium
import pandas

data=data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=[80, -100])
print(map)
#map.save("Map1.html")
#map=folium.Map(location=[38.58, -99.09])
#map.save("Map1.html")
#map=folium.Map(location=[38.58, -99.09],zoom_start=6)
#map.save("Map1.html")
#tiles="Stamen Terrain"
#map=folium.Map(location=[38.58, -99.09],zoom_start=6,tiles="Stamen Terrain")
#map.save("Map1.html")
map=folium.Map(location=[38.58, -99.09],zoom_start=6,tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Volcanoes")

for lt, ln,el in zip(lat,lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],radius=6, popup=folium.Popup(str(el)+"m"),
    fill_color=color_producer(el),color='grey',fill_opacity=0.7,fill=True))
    
fgp=folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green'if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
      
#adding markers multiple times
#fg.add_child(folium.Marker(location=[37.2, -97.1], popup="Hi I am a Marker",icon=folium.Icon(color='green')))


map.save("Map1.html")

