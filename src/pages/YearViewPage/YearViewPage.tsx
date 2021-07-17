import React from 'react';
import Map from '@components/Map';
import ResultsHeader from '@components/ResultsHeader';

import './YearViewPage.css'

let YearViewPage: React.FunctionComponent = () => {
    return (
        <div>
            <ResultsHeader/>
            <Map/>
        </div>
    );
}

export default YearViewPage;
