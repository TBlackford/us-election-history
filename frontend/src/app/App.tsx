import React, { FunctionComponent, useEffect } from 'react';
import { useDispatch } from "react-redux";

import { initialise} from '@slices/years';
import Router from "@app/Router";

import './App.css';


const App: FunctionComponent = () => {
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(initialise());
    }, [dispatch]);

    return (
        <div className="main-content">
            <Router />
        </div>
    );
}

export default App;
