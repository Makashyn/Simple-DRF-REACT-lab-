import React, { Component } from 'react';
import navigateTo from '../nav.js';
import PropTypes from 'prop-types';
import './App.css';



export default class Ticket extends Component {

	ticketDetail = (id) => {
		if (window.location.pathname === '/'){
			navigateTo('/ticket/' + id)
		}
	}

	convertMonth = (number) => {
		const month_array = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'];
		return month_array[number];
	}

	render() {

		const { ticket }  = this.props;
		const showDetail = this.props.showDetail || false;

		const start_date_time = new Date(ticket.start_date).toLocaleTimeString();
		const end_date_time = new Date(ticket.end_date).toLocaleTimeString();
		const start_date = new Date(ticket.start_date).getDate();
		const start_month = new Date(ticket.start_date).getMonth();

		return (
			<div>
				<div className='ticket-container'>
					<div class='ticket-left'>
						<div className='airline'>{ ticket.airline.name }</div>
						<div className='ticket-time'>
							<span>{ start_date_time }</span>
							<span> - { end_date_time }</span>
						</div>
						<div className='ticket-info'>
							<div>{ start_date } {this.convertMonth(start_month)}</div>
							<div className='tickets-city'>
								<span className='ticket-start-city'>{ ticket.start_city.name }</span>
								<span className='ticket-end-city'> - { ticket.end_city.name }</span>
							</div>
						</div>
					</div>
					<div className='ticket-price-relative'>
						<div className='ticket-price'>{ ticket.price }</div>
					</div>
				</div>
				
			</div>
		)
	}
}


Ticket.propTypes = {
	ticket: PropTypes.object,
	showDetail: PropTypes.bool
};