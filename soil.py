import requests

def main():
    longitude = input("longitude")
    latitude = input("latitude")
    url = f"http://www.landis.org.uk/arcgis/rest/services/Utilities/Geometry/GeometryServer/project?f=json&outSR=27700&inSR=4326&geometries=%7B%22geometryType%22%3A%22esriGeometryPoint%22%2C%22geometries%22%3A%5B%7B%22x%22%3A{latitude}%2C%22y%22%3A{longitude}%2C%22spatialReference%22%3A%7B%22wkid%22%3A4326%7D%7D%5D%7D"
    print(url)
    j = requests.get(url).json()
    print(j)

    x = j["geometries"][0]["x"]
    y = j["geometries"][0]["y"]
    geometry = f"%7B%22x%22%3A{x}%2C%22y%22%3A{y}%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%7D%7D"
    url = f"http://www.landis.org.uk/arcgis/rest/services/Soilscapes/soilscapes/MapServer/0/query?f=json&where=&returnGeometry=true&spatialRel=esriSpatialRelIntersects&maxAllowableOffset=20&geometry={geometry}&geometryType=esriGeometryPoint&inSR=102100&outFields=SS_ID%2CDRAINAGE%2CFERTILITY%2CArea&outSR=102100"

    print(f"requesting url: {url}")
    j = requests.get(url).json()
    print(j)

if __name__ == "__main__":
    main()
