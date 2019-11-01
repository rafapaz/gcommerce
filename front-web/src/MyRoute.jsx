import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import Home from './Home';
import About from './About';
import Login from './Login';
import Logout from './Logout';
import Erro404 from './Erro404';


class MyRoute extends React.Component {
    render() {
        //const username = localStorage.getItem('@todo-app/username');
        
        return (            
                <BrowserRouter>
                    <Switch>
                        <Route path='/' exact={true} component={Home} />
                        <Route path='/about' component={About} />
                        <Route path='/logout' component={Logout} />
                        <Route path='/login' exact={true} component={Login} />
                        <Route path="*" component={Erro404} />                            
                    </Switch>
                </BrowserRouter>
        );
                
    }
}

export default MyRoute;