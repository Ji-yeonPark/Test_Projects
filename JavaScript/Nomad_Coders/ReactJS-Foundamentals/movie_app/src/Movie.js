// import React, { Component } from 'react';
import React from 'react';
import PropTypes from 'prop-types';
import './Movie.css';

// class Movie extends Component {

//     static propTypes = {
//         title: PropTypes.string.isRequired,
//         poster: PropTypes.string.isRequired
//     }

//     render() {
//         console.log(this.props)

//         return (
//             <div>
//                 <MoviePoster poster={this.props.poster}/>
//                 <h1>{this.props.title}</h1>
//             </div>
//         )
//     }
// }

function Movie({ title, poster }) {
    return (
        <div>
            <MoviePoster poster={poster} />
            <h1>{title}</h1>
        </div>
    )
}

Movie.propTypes = {
    title: PropTypes.string.isRequired,
    poster: PropTypes.string.isRequired
}

// class MoviePoster extends Component {

//     static propTypes = {
//         poster: propTypes.string.isRequired
//     }
//     render () {
//         return (
//             <img src={this.props.poster} alt="Movie Poster"></img>
//         )
//     }
// }

function MoviePoster({ poster }) {
    return (
        <img src={poster} alt="Movie Poster"></img>
    )
}

MoviePoster.propTypes = {
    poster: PropTypes.string.isRequired
}

export default Movie;