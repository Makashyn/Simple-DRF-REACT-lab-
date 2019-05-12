import React, { Component } from 'react';
import TicketsList from '../TicketsList';
import Header from '../Header';
import SearchBar from 'material-ui-search-bar';
import './style.css';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';

const styles = theme => ({
  root: {
    display: 'flex',
  },
  formControl: {
    margin: theme.spacing.unit * 3,
  },
});


export default class MainPage extends Component {
	state = {
		searchRequest: ''
	}

	setSearchRequest = (request) => {
		this.setState({
			searchRequest: request,
		});
	}

	render() {
		return(
			<div>
				<Header setSearchRequest={this.setSearchRequest}/>
				<div id="main-page">
				 	<div>
						<TicketsList searchRequest={this.state.searchRequest}/>
					</div>
				</div>
			</div>
		)	
		
	}
}