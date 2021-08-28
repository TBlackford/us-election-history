import React from 'react';
import { RouteComponentProps, withRouter } from "react-router-dom";
import Map from '@components/Map';
import ResultsHeader from '@components/ResultsHeader';

let YearViewPage: (props: RouteComponentProps) => JSX.Element = (props) => {
    // @ts-ignore
    let year: string = props.match.params['year'].toString() || '';
    return (
        <>
            <ResultsHeader/>
            <Map year={year}  />
        </>
    );
}

export default withRouter(YearViewPage);
