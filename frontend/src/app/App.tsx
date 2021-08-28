import React, { Component } from 'react';
import Router from "@app/Router";

import './App.css';


class App extends Component {
    render() {
        return (
            <div className="main-content">
                <Router />
            </div>
        );
    }
}

export default App;
