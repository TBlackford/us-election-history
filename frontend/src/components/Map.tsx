import React, { PropsWithChildren, useEffect, useState } from 'react';
import { geoAlbersUsa, geoPath, GeoPermissibleObjects } from 'd3-geo';

import cartographer from "@common/cartographer.api";
import LoadingBar from "@components/LoadingBar";

const width = 800;
const height = 450;

const projection = geoAlbersUsa()
    .scale(950)
    .translate([width / 2, height / 2]);

interface IGeoJsonObject {
    features: [],
    type: string,
}

interface MapParams {
    year: string;
}


const Map: React.FunctionComponent<MapParams> = (props: PropsWithChildren<MapParams>) => {
    // Map data to be displayed
    const [geojson, setGeojson] = useState<IGeoJsonObject>({
        features: [],
        type: ""
    });
    const [isLoading, setIsLoading] = useState<boolean>(true);

    // Get the data from the git repo (cheeky way to do an api I don't have to pay for or maintain)
    useEffect(() => {
        cartographer('GET', props.year.toString(), {})
            .then(res => {
                console.log("before set");
                setGeojson(res.data.map);
                setIsLoading(false);
                console.log("after set");
            })
            .catch(error => {
                if(error.response) {
                    console.log(error.response.data);
                    console.log(error.response.status);
                    console.log(error.response.headers);
                }
            })
    }, [props.year]);

    const handleCountryClick = (countryIndex: number) => {
        // TODO: flesh this out
        console.log("Clicked on country: ", geojson.features[countryIndex]['properties']['LABEL']);
    }

    const handleCountryMouseEnter = (countryIndex: number) => {
        // TODO: make this
    }

    return (
        // eslint-disable-next-line no-mixed-operators
        isLoading && <LoadingBar /> ||
        <svg width={800} height={450} viewBox={`0 0 ${width} ${height}`} className="m-auto">
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
