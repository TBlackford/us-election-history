import React, {FunctionComponent, useEffect} from 'react'
import { Router, RouteComponentProps, Link } from "@reach/router"

import HomePage from "./pages/HomePage";
import YearViewPage from "./pages/YearViewPage";

import './App.css';

type Props = { component: FunctionComponent } & RouteComponentProps;

const Route: FunctionComponent<Props> = ({ component: Component, ...rest }) => (
    <Component {...rest} />
);

const App: React.FunctionComponent = (props) => {
    return (
        <div className="container">
            <Router>
                <Route path="/" component={HomePage} />
                <Route path="/" component={YearViewPage} />
            </Router>
        </div>
    );
};


export default App;
