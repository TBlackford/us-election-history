import json

map_list = {
    '1788': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1789030.geojson',
    '1792': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1792060.geojson',
    '1796': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1796060.geojson',
    '1800': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1800100.geojson',
    '1804': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1804100.geojson',
    '1808': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1805070.geojson',
    '1812': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1812060.geojson',
    '1816': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1813040.geojson',
    '1820': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1820030.geojson',
    '1824': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1822030.geojson',
    '1828': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1828050.geojson',
    '1832': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1828050.geojson',
    '1836': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1836070.geojson',
    '1840': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1838070.geojson',
    '1844': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1842110.geojson',
    '1848': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1848080.geojson',
    '1852': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1850090.geojson',
    '1856': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1854050.geojson',
    '1860': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1860020.geojson',
    '1864': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1864100.geojson',
    '1868': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1868073.geojson',
    '1872': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1872100.geojson',
    '1876': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1876080.geojson',
    '1880': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1876080.geojson',
    '1884': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1884050.geojson',
    '1888': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1884050.geojson',
    '1892': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1890071.geojson',
    '1896': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1896050.geojson',
    '1900': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1900060.geojson',
    '1904': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1903100.geojson',
    '1908': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1907110.geojson',
    '1912': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1912080.geojson',
    '1916': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1912080.geojson',
    '1920': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1912080.geojson',
    '1924': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1921030.geojson',
    '1928': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1921030.geojson',
    '1932': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1921030.geojson',
    '1936': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1921030.geojson',
    '1940': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1921030.geojson',
    '1944': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1921030.geojson',
    '1948': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1921030.geojson',
    '1952': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1921030.geojson',
    '1956': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1921030.geojson',
    '1960': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '1964': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '1968': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '1972': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '1976': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '1980': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '1984': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '1988': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '1992': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '1996': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '2000': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '2004': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '2008': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '2012': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '2016': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
    '2020': 'https://api.github.com/repos/TBlackford/us-history-maps/contents/GeoJSON/1959080.geojson',
}

def make_response(status, body = {}):
    return {
        "statusCode": status,
        "body": json.dumps(body)
    }

def hello(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def get_map(event, context):
    map_path = event['pathParameters']['year']
    if map_path is not None:
        if map_path in map_list:
            return make_response(200, {
                "map": map_list[map_path]
            })
        else:
            return make_response(404, {
                "msg": "Year does not exist"
            })
    else:
        return make_response(500, {
                "msg": "Enter a year"
            })