import React, { CSSProperties, PropsWithChildren, useEffect, useState } from 'react';
import { geoAlbersUsa, geoPath, GeoPermissibleObjects } from 'd3-geo';

import cartographer from "@common/cartographer.api";
import LoadingBar from "@components/LoadingBar";

const projection = (width: number, height: number) => geoAlbersUsa()
    .scale(950)
    .translate([width / 2, height / 2]);

interface IGeoJsonObject {
    features: [],
    type: string,
}

interface MapParams {
    year?: string
    width?: number;
    height?: number;
}

class SvgCSS implements CSSProperties, MapParams {
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
        cartographer('GET', props?.year?.toString(), {})
            .then(res => {
                setGeojson(res.data.map);
                setIsLoading(false);
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

    const width = props.width ?? 0;
    const height = props.height ?? 0;

    return (
        // eslint-disable-next-line no-mixed-operators
        isLoading && <LoadingBar /> ||
        <svg style={{width: '100%', height: '100%', overflow: 'visible'} as SvgCSS}
             viewBox={`0 0 800 450`} className="m-auto">
            <g className="countries" transform={`translate(${width / 2}, ${height / 2})`}>
                {
                    geojson.features.map((d: GeoPermissibleObjects, i: any) => (
                        <path
                            key={`path-${i}`}
                            // @ts-ignore
                            d={geoPath().projection(projection(props.width, props.height))(d)}
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

Map.defaultProps = {
    year: '1788',
    width: 800,
    height: 450
}

export default Map;
