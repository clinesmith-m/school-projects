import React from 'react';
import ReactDOM from 'react-dom';

class Posts extends React.Component {
	constructor(props) {
		super(props);

		this.state = {
			posts: [],
			loaded: false,
			login: true,
			error: null
		};
	}

	componentDidMount() {
		window.fetch('/api/render-post/')
		.then(res => res.json())
		.then(
			(result) => {
				this.setState({
					loaded: true,
					posts: result
				});
			},
			(error) => {
				this.setState({
					loaded: true,
					error: error,
				});
			},
		);
	}

	render() {
		if (this.state.error) {
			return <div>Oops! Ran into some trouble there.</div>
		} else if (!this.state.loaded) {
			return <div>Sorry! Failed to load posts.</div>
		} else {
			return (
				<div className="minutes-post">
					<h1>Past Minutes</h1>
					<ul className="minutes-post">
					{this.state.posts.map(post => (
						<li className="minutes-post" key={post.id}>
							<h3>{post.date}</h3>
							<a  href={'/static/minutes/' + post.filepath}>MINUTES</a>
						</li>
					))}
					</ul>
				</div>
			);
		}
	}
}

class Images extends React.Component {
	constructor(props) {
		super(props);

		this.state = {
			images: [],
			loaded: false,
			login: true,
			error: null,
			active: true,
		};
	}

	componentDidMount() {
		window.fetch('/api/render-image/')
		.then(res => res.json())
		.then(
			(result) => {
				this.setState({
					loaded: true,
					posts: result
				});
			},
			(error) => {
				this.setState({
					loaded: true,
					error: error,
				});
			},
		);
	}

	handleTabChange() {
		this.setState({
			active: false, // This doesn't do anything. It's just a placeholder.
		});
	}

	render() {
		if (this.state.error) {
			return <div>Oops! Ran into some trouble there.</div>
		} else if (!this.state.loaded) {
			return <div>Sorry! Failed to load posts.</div>
		} else {
			return (
				<div className="image-post">
					<div className="navbar">
						<button
							id="post-button"
							onClick={(evt) => {
								evt.preventDefault();
								this.handleTabChange();
						}}>Minutes</button>
					</div>
					<h1>Past Minutes</h1>
					<ul className="image-post">
					{this.state.posts.map(post => (
						<li className="image-post" key={post.id}>
							<h3>{post.title}</h3>
							<img  src={'/static/img/' + post.filepath}></img>
						</li>
					))}
					</ul>
				</div>
			);
		}
	}
}

class Upload extends React.Component {
	constructor(props) {
		super(props)
		this.state = {
			useradmin: true,
		};	
	}
	
	upload() {
		var data = new FormData();
		var imagedata = document.querySelector('#img-form');
		
		window.fetch('/', {
			method: "POST",
			headers: {
				"Content-Type": "multipart/form-data",
				"Accept": "application/json",
				"type": "formData"
			},
			body: data
		})
		.then(function (res) {
			if (res.status == 200) {
				return console.log('Its alive!');
			} else if (res.status == 401) {
				return console.log('Dang!');
			}
		},
		function (e) {
			alert("Error submitting from.");
		});
	}

	render() {
		/*if (this.useradmin) {
			return (
				<div className="admin-post">
					<form encType="multipart/form-data" action="" method="POST">
						<h3>Upload an image!</h3>
						<div className="form-group">
							<label htmlFor="title">Title</label>
							<input type="text" className="form-control" id="title" name="title"></input>
						</div>
						<div className="form-group">
							<input type="file" id="imagefile" name="imagefile"></input>
						</div>
						<div className="form-group">
							<input type="text" className="form-group" id="tags" name="tags" placeholder="tag 1, tag 2, tag 3, etc..."></input>
						</div>
						<button value="submit" onClick={this.upload.bind(this)}>Post</button>
					</form>
					<form encType="multipart/form-data" action="" method="POST">
						<h3>Upload meeting minutes!</h3>
						<div className="form-group">
							<label htmlFor="date">Date (MM/YYYY)</label>
							<input type="text" className="form-control" id="date" name="date"></input>
						</div>
						<div className="form-group">
							<input type="file" id="minfile" name="minfile"></input>
						</div>
						<button value="submit" onClick={this.upload.bind(this)}>Post</button>
					</form>	
					<form encType="multipart/form-data" action="" method="POST">
						<h3>Update the Club Constitution!</h3>
						<div className="form-group">
							<input type="file" id="constitution" name="constitution"></input>
						</div>
						<button value="submit" onClick={this.upload.bind(this)}>Post</button>
					</form>	
				</div>
			)
		}
		else {*/
			return (
				<div className="normie-post">
					<form encType="multipart/form-data" action="" id="img-form">
						<h3>Upload an image!</h3>
						<div className="form-group">
							<label htmlFor="title">Title</label>
							<input type="text" className="form-control" id="title" name="title"></input>
						</div>
						<div className="form-group">
							<input type="file" id="imagefile" name="imagefile"></input>
						</div>
						<div className="form-group">
							<input type="text" className="form-group" id="tags" name="tags" placeholder="tag 1, tag 2, tag 3, etc..."></input>
						</div>
						<button value="submit" onClick={this.upload.bind(this)}>Post</button>
					</form>
				</div>
			)
		//}
	}
}

class App extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			view: 'images'
		};
	}

	showMinutes() {
		this.setState({
			view: 'minutes'
		});
	}

	render() {
		let component = (this.state.view === 'images')
				? <Images showMinutes={() => this.showMinutes()} />
				: <Posts />; 
			
		return (
			<div className="app">{component}</div>
		);
	}
}


ReactDOM.render(<Images />, document.getElementById('content'));
