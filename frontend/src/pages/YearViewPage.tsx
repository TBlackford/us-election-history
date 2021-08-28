import React, { FunctionComponent } from 'react';
import { useParams, withRouter } from "react-router-dom";
import Map from '@components/Map';
import ResultsHeader from '@components/ResultsHeader';

const years: Array<string | undefined> =
    Array.from(new Array(59),(val, index) => ((index * 4) + 1788).toString() );

interface SlugParams {
    year?: string | undefined
}

const YearViewPage: FunctionComponent = () => {
    const { year } = useParams<SlugParams>();

    Notification.requestPermission()
        .then(() => new Notification('Hey 👋'));

    if(!years.includes(year)) {
        return null;
    }

    return (
        <>
            <ResultsHeader/>
            <Map year={year} width={800} height={450} />
        </>
    );
}

export default withRouter(YearViewPage);
