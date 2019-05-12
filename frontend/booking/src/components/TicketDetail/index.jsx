import React, { Component } from 'react';
import './style.css';
import axios from 'axios';
import Project from '../Project';
import ProjectTableHeader from '../ProjectTableHeader';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
class ProjectDetail extends Component {
	state = {
		project: [],
		isLoaded: false,
	}
	componentDidMount() {
		const projectId = this.props.match.params.id;
		axios.get(`/api/projects/?id=${projectId}`)
			.then(res => {
				this.setState({
					project: res.data,
					isLoaded: true
				})
			})
	}
	render() {
		
		if (!this.state.isLoaded){
			return <div> Loading... </div>;
		}
		else {
			const project = this.state.project.results[0]
			return(
				<div className='projects-list'>
					<Table>
						<ProjectTableHeader />
						<TableBody>
							<Project  project = {project} showDetail={true}	/> 
						</TableBody>
					</Table>
				</div>
			)
		}
	}
}

export default ProjectDetail