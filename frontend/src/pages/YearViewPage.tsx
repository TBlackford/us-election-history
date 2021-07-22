import React from 'react';
import { RouteComponentProps } from "react-router-dom";
import Map from '@components/Map';
import ResultsHeader from '@components/ResultsHeader';

import './YearViewPage.css'

let YearViewPage: (props: RouteComponentProps) => JSX.Element = (props) => {
    // @ts-ignore
    let year: string = props.match.params['year'].toString() || '';
    return (
        <div>
            <ResultsHeader/>
            <Map year={year}/>
        </div>
    );
}

export default YearViewPage;
