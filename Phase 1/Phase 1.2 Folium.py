def create_map(df_municipios):
    spain = folium.Map(location=(39, -4), zoom_start=7)
    minimap = plugins.MiniMap(toggle_display=False, position='bottomleft')
    spain.add_child(minimap)
    plugins.ScrollZoomToggler().add_to(spain)
    plugins.Fullscreen(position='topright').add_to(spain)

    for (index, row) in df_municipios.iterrows():
        folium.Marker(location=[row['latitud'], row['longitud']],
                      popup=row['capital'], tooltip='click').add_to(spain)

    return spain

create_map(df_municipios)