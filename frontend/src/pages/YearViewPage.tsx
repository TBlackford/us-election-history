import React, { FunctionComponent, useEffect, useState } from 'react';
import { Redirect, useParams, withRouter } from "react-router-dom";
import Map from '@components/Map';
import ResultsHeader from '@components/ResultsHeader';

import { useAppSelector } from "@app/hooks";

interface SlugParams {
    year?: string | undefined
}

const YearViewPage: FunctionComponent = () => {
    const [redirect, setRedirect] = useState(false);
    const { year } = useParams<SlugParams>();
    const years = useAppSelector((state) => state.years.list)

    useEffect(() => {
        console.log(year);
        console.log(years);
        if(!years.includes(year) && years.length !== 0) {
            setRedirect(true);
        }
    }, [year, years])

    return redirect && <Redirect to={'404'} /> || (
        <>
            <ResultsHeader/>
            <div style={{width: "800px", height: "450px"}}>
                <Map year={year} width={800} height={450} />
            </div>
        </>
    );
}

export default withRouter(YearViewPage);
