import React, { PropsWithChildren } from 'react';

import './YearViewPage.css'
import Map from "../../components/Map";
import ResultsHeader from "../../components/ResultsHeader";

let YearViewPage: React.FunctionComponent = (props: PropsWithChildren<{}>) => {
    return (
        <div>
            <ResultsHeader />
            <Map />
        </div>
    );
}

export default YearViewPage;
