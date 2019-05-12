import React, { Component } from 'react';
import Ticket from '../Ticket';
import axios from 'axios';
import './style.css';

import TicketListPagination from '../TicketListPagination'


class TicketsList extends Component {
	state = {
		tickets: [],
		isLoaded: false,
	}

	componentDidMount() {
		axios.get(`/api/tickets/`)
			.then(res => {
				console.log(res);
				this.setState({
					tickets: res.data,
					isLoaded: true
				})
			})
	}

	getPageData = (url) => {
		axios.get(url)
			.then(res => {
				this.setState({
					tickets: res.data,
					isLoaded: true
				})
			})
	}

	componentDidUpdate(prevProps) {
		if (prevProps != this.props){
			this.setState({
				isLoaded: false
			})
			var filter = '';


			filter = '?search=' + this.props.searchRequest;

			axios.get(`api/tickets/${filter}`)

			.then(res => {
				this.setState({
					tickets: res.data,
					isLoaded: true
				})
			})
		}
	}

	render() {

		if (!this.state.isLoaded){
			return <div> Loading... </div>;
		}
		else {
			const ticketElements = this.state.tickets.results.map((ticket) =>
				<Ticket key = {ticket.id}  ticket = {ticket}/> 
			)
			return(
				<div className="tickets-list ticket-list-main-page">
					{ticketElements}
				

				</div>
			);
		}	
	}
}

export default TicketsList;
