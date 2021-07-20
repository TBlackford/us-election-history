from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Cheekily, I just return a dict to a GitHub repo.
# This is intended to change to a proper S3 bucket later.
maps = {
    '1788': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1789030.geojson',
    '1792': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1792060.geojson',
    '1796': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1796060.geojson',
    '1800': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1800100.geojson',
    '1804': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1804100.geojson',
    '1808': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1805070.geojson',
    '1812': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1812060.geojson',
    '1816': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1813040.geojson',
    '1820': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1820030.geojson',
    '1824': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1822030.geojson',
    '1828': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1828050.geojson',
    '1832': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1828050.geojson',
    '1836': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1836070.geojson',
    '1840': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1838070.geojson',
    '1844': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1842110.geojson',
    '1848': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1848080.geojson',
    '1852': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1850090.geojson',
    '1856': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1854050.geojson',
    '1860': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1860020.geojson',
    '1864': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1864100.geojson',
    '1868': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1868073.geojson',
    '1872': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1872100.geojson',
    '1876': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1876080.geojson',
    '1880': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1876080.geojson',
    '1884': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1884050.geojson',
    '1888': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1884050.geojson',
    '1892': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1890071.geojson',
    '1896': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1896050.geojson',
    '1900': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1900060.geojson',
    '1904': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1903100.geojson',
    '1908': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1907110.geojson',
    '1912': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1912080.geojson',
    '1916': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1912080.geojson',
    '1920': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1912080.geojson',
    '1924': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1921030.geojson',
    '1928': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1921030.geojson',
    '1932': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1921030.geojson',
    '1936': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1921030.geojson',
    '1940': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1921030.geojson',
    '1944': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1921030.geojson',
    '1948': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1921030.geojson',
    '1952': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1921030.geojson',
    '1956': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1921030.geojson',
    '1960': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '1964': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '1968': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '1972': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '1976': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '1980': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '1984': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '1988': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '1992': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '1996': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '2000': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '2004': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '2008': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '2012': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '2016': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
    '2020': 'https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1959080.geojson',
}

@app.route("/<year:int>")
def hello_from_root(year):
    return make_response(jsonify(maps[year]), 200)


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
