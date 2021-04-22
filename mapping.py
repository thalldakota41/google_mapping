import folium 
map = folium.Map(location=[54.2361, 4.5481], zoom_start=6) 

map.add_child(folium.Marker(location=[54.23, 4.54], popup="I have been here", icon=folium.Icon(color='green')))

map.save("Map1.html")