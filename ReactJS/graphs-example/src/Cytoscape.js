import React, {Component} from 'react';
import cytoscape from 'cytoscape';
//import conf from './conf';

let cyStyle = {
  height: '400px',
  display: 'block'
};

class Cytoscape extends Component{
  cy = null;

  componentDidMount(){
    // conf.container = this.refs.cyelement;
    // let cy = cytoscape(conf);

    // this.cy = cy;
    // cy.json({elements: this.props.elements});
  }

  shouldComponentUpdate(){
    return false;
  }

  componentWillReceiveProps(nextProps){
    this.cy.json(nextProps);
  }

  componentWillUnmount(){
    this.cy.destroy();
  }

  getCy(){
    return this.cy;
  }

  render(){
    return <div style={cyStyle} ref="cyelement" />
  }
}

export default Cytoscape;