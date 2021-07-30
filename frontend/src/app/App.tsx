import React from 'react';
import { Route, RouteComponentProps, RouteProps, Switch, withRouter } from 'react-router-dom';

import HomePage from "../pages/HomePage";
import YearViewPage from "../pages/YearViewPage";

import './App.css';

interface RenderProps extends RouteProps {
}

interface HistoryProps extends RouteComponentProps {
}

const NoMatch = () => (
    <div>
        Page Not Found
    </div>
)

class App extends React.Component<RenderProps & HistoryProps> {
    render() {
        return (
            <div className="main-content">
                <div>
                    <Switch>
                        <Route exact path="/" component={HomePage}/>
                        <Route exact path="/:year/" component={YearViewPage}/>
                        <Route path="*">
                            <NoMatch/>
                        </Route>
                    </Switch>
                </div>
            </div>
        );
    }
}

export default withRouter(App);
