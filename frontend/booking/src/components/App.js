import React, { Component } from 'react';
import { Route } from 'react-router-dom';

import '../index.css'
import MainPage from './MainPage';
import appMui from './appMui.jsx';
// import '../config/axios.js';

class App extends Component {

	render() {
    	return (
    		<div className="App">
				<MainPage />
    	  	</div>	
    	)
  	}
}

export default appMui(App);
