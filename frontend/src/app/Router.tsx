import React, { FunctionComponent } from 'react';
import { Route, Switch } from 'react-router-dom';

// Pages
import HomePage from "@pages/HomePage";
import YearViewPage from "@pages/YearViewPage";

const NoMatch = () => (
    <div>
        Page Not Found
    </div>
)


const Router: FunctionComponent = () => {
    return (
        <Switch>
            <Route exact path="/" component={HomePage}/>
            <Route exact path="/:year([0-9]{4})" component={YearViewPage}/>

            <Route path="*">
                <NoMatch/>
            </Route>
        </Switch>
    )
}

export default Router;
