import json
import boto3

s3 = boto3.client('s3')

map_list = {
    '1788': 'GeoJSON/1789030.geojson',
    '1792': 'GeoJSON/1792060.geojson',
    '1796': 'GeoJSON/1796060.geojson',
    '1800': 'GeoJSON/1800100.geojson',
    '1804': 'GeoJSON/1804100.geojson',
    '1808': 'GeoJSON/1805070.geojson',
    '1812': 'GeoJSON/1812060.geojson',
    '1816': 'GeoJSON/1813040.geojson',
    '1820': 'GeoJSON/1820030.geojson',
    '1824': 'GeoJSON/1822030.geojson',
    '1828': 'GeoJSON/1828050.geojson',
    '1832': 'GeoJSON/1828050.geojson',
    '1836': 'GeoJSON/1836070.geojson',
    '1840': 'GeoJSON/1838070.geojson',
    '1844': 'GeoJSON/1842110.geojson',
    '1848': 'GeoJSON/1848080.geojson',
    '1852': 'GeoJSON/1850090.geojson',
    '1856': 'GeoJSON/1854050.geojson',
    '1860': 'GeoJSON/1860020.geojson',
    '1864': 'GeoJSON/1864100.geojson',
    '1868': 'GeoJSON/1868073.geojson',
    '1872': 'GeoJSON/1872100.geojson',
    '1876': 'GeoJSON/1876080.geojson',
    '1880': 'GeoJSON/1876080.geojson',
    '1884': 'GeoJSON/1884050.geojson',
    '1888': 'GeoJSON/1884050.geojson',
    '1892': 'GeoJSON/1890071.geojson',
    '1896': 'GeoJSON/1896050.geojson',
    '1900': 'GeoJSON/1900060.geojson',
    '1904': 'GeoJSON/1903100.geojson',
    '1908': 'GeoJSON/1907110.geojson',
    '1912': 'GeoJSON/1912080.geojson',
    '1916': 'GeoJSON/1912080.geojson',
    '1920': 'GeoJSON/1912080.geojson',
    '1924': 'GeoJSON/1921030.geojson',
    '1928': 'GeoJSON/1921030.geojson',
    '1932': 'GeoJSON/1921030.geojson',
    '1936': 'GeoJSON/1921030.geojson',
    '1940': 'GeoJSON/1921030.geojson',
    '1944': 'GeoJSON/1921030.geojson',
    '1948': 'GeoJSON/1921030.geojson',
    '1952': 'GeoJSON/1921030.geojson',
    '1956': 'GeoJSON/1921030.geojson',
    '1960': 'GeoJSON/1959080.geojson',
    '1964': 'GeoJSON/1959080.geojson',
    '1968': 'GeoJSON/1959080.geojson',
    '1972': 'GeoJSON/1959080.geojson',
    '1976': 'GeoJSON/1959080.geojson',
    '1980': 'GeoJSON/1959080.geojson',
    '1984': 'GeoJSON/1959080.geojson',
    '1988': 'GeoJSON/1959080.geojson',
    '1992': 'GeoJSON/1959080.geojson',
    '1996': 'GeoJSON/1959080.geojson',
    '2000': 'GeoJSON/1959080.geojson',
    '2004': 'GeoJSON/1959080.geojson',
    '2008': 'GeoJSON/1959080.geojson',
    '2012': 'GeoJSON/1959080.geojson',
    '2016': 'GeoJSON/1959080.geojson',
    '2020': 'GeoJSON/1959080.geojson',
}

def make_response(status, body = {}):
    return {
        "statusCode": status,
        "body": json.dumps(body, sort_keys=True, default=str),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials" : True,
            'Access-Control-Allow-Methods': 'OPTIONS,GET'
        },
    }

def from_bucket(key):
    bucket = s3.get_object(Bucket='us-history-maps', Key=key)
    return json.loads(bucket['Body'].read().decode("utf-8"))

def hello(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def get_map(event, context):
    map_path = event['pathParameters']['year']
    if map_path is not None:
        if map_path in map_list:
            return make_response(200, {
                "map": from_bucket(map_list[map_path])
            })
        else:
            return make_response(404, {
                "msg": "Year does not exist"
            })
    else:
        return make_response(500, {
                "msg": "Enter a year"
            })

def get_all_maps(event, context):
    # This won't work -> too much data to get and it times out
    maps = {}

    for year, map_path in map_list.items():
        maps[year] = from_bucket(map_path)

    return make_response(200, {
        "maps": maps
    })

def get_all_years(event, context):
    return make_response(200, {
        "years": [years for years in map_list.keys()]
    })

def buckets(event, context):
    bucket = s3.get_object(Bucket='us-history-maps', Key='GeoJSON/1789030.geojson')

    response_payload = json.loads(bucket['Body'].read().decode("utf-8"))

    return make_response(200, response_payload)