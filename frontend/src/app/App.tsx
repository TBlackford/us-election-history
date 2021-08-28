import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';

import HomePage from "../pages/HomePage";

import './App.css';

const NoMatch = () => (
    <div>
        Page Not Found
    </div>
)

class App extends Component {
    render() {
        return (
            <div className="main-content">
                <div>
                    <Switch>
                        <Route exact path="/" component={HomePage}/>
                        <Route path="*">
                            <NoMatch/>
                        </Route>
                    </Switch>
                </div>
            </div>
        );
    }
}

export default App;
