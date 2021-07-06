import React, { useEffect } from 'react'
import { Router, RouteComponentProps, Link } from "@reach/router"

import './App.css';

let Home = (props: RouteComponentProps) => <div>Home</div>
let Dash = (props: RouteComponentProps) => <div>Dash</div>


const App: React.FunctionComponent = (props) => {
    return (
        <div className="main-content">
            <Router>
                <Home path="/" />
                <Dash path="dashboard" />
            </Router>
        </div>
    );
};


export default App;
