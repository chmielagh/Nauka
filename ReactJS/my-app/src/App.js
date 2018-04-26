import React, { Component } from 'react';
import './App.css';
import Graph from './Graph/Graph'
import Radium from 'radium'

class App extends Component {

  render() {
    return (
      <div className="App">
        <Graph/>
      </div>
    );
  }
}

export default Radium(App);
