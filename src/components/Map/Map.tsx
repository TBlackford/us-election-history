import React, {Component, PropsWithChildren, useEffect, useState} from 'react';
import {geoAlbersUsa, geoMercator, geoPath, GeoPermissibleObjects} from 'd3-geo';
import axios from 'axios';
import './Map.css'

const width = 800;
const height = 450;

const projection = geoAlbersUsa()
    .scale(950)
    .translate([width/2, height/2]);

interface IGeoJsonObject {
    features: [],
    type: string,
}

const Map: React.FunctionComponent = () => {
    // Map data to be displayed
    const [geojson, setGeojson] = useState<IGeoJsonObject>({
        features: [],
        type: ""
    });

    // Get the data from the git repo (cheeky way to do an api I don't have to pay for or maintain)
    useEffect(() => {
        axios.get('https://raw.githubusercontent.com/TBlackford/us-history-maps/master/GeoJSON/1789030.geojson')
            .then(res => {
                console.log(res.data);
                setGeojson(res.data);
            })
    }, []);

    const handleCountryClick = (countryIndex: number) => {
        // TODO: flesh this out
        console.log("Clicked on country: ", geojson.features[countryIndex]['properties']['LABEL']);
    }

    const handleCountryMouseEnter = (countryIndex: number) => {
        // TODO: make this
    }

    return (
        <svg width={800} height={450} viewBox={`0 0 ${width} ${height}`}>
            <g className="countries">
                {
                    geojson.features.map((d: GeoPermissibleObjects, i: any) => (
                        <path
                            key={`path-${i}`}
                            // @ts-ignore
                            d={geoPath().projection(projection)(d)}
                            className="country"
                            stroke="#FFFFFF"
                            strokeWidth={0.5}
                            onClick={() => handleCountryClick(i)}
                            onMouseEnter={() => handleCountryMouseEnter(i)}
                        />
                    ))
                }
            </g>
        </svg>
    )//*/
}

export default Map;
