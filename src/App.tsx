import React from 'react';
import { Route, Switch, RouteProps, RouteComponentProps, withRouter } from 'react-router-dom';

import HomePage from "./pages/HomePage";
import YearViewPage from "./pages/YearViewPage";

import './App.css';

interface RenderProps extends RouteProps {
    /* other props for ChildComponent */
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
                        <Route path="/:year" component={YearViewPage}/>
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

export default withRouter(App);
