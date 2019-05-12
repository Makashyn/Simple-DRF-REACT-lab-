import { Pager } from 'react-bootstrap';
import React from 'react';
import PropTypes from 'prop-types';
import './App.css' 

const TicketListPagination = ({ getPageData, next, previous}) => {

	return(
		<Pager>
			{previous ? (
					<Pager.Item  onClick={() => getPageData(previous.slice(previous.indexOf('/api'), previous.length))}>Previous</Pager.Item>
				) : (
					<Pager.Item  disabled >Previous</Pager.Item>
			)}
			{next ? (
					<Pager.Item  onClick={() => getPageData(next.slice(next.indexOf('/api'), next.length))}>Next</Pager.Item>
				) : (
					<Pager.Item  disabled >Next</Pager.Item>
			)}
		</Pager>
	)
};

TicketListPagination.propTypes = {
	getPageData: PropTypes.func,
	next: PropTypes.string,
	previous: PropTypes.string 
};

export default TicketListPagination
