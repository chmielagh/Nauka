import React, {Component} from 'react';
import Node from './Node/Node';
import Radium from 'radium';

class Block extends Component {
    state = {
        iter: 0,
        nodes: [
            {id: '0', label: 'first'},
            {id: '1', label: 'secound'}
        ]
    }

    addNode = () => {
        console.log('add Node');
    }

    wordChangedHandler = (event) => {
        this.setState({
            nodes: [
                {id: '0', label: event.target.value},
                {id: '1', label: 'secound'}
            ]
        })
    }

    render(){
        return (
            <div className='Block'>
                <Node text={this.state.nodes[0].label} changed={this.wordChangedHandler}/>
                <Node text={this.state.nodes[1].label} changed={this.wordChangedHandler}/>
            </div>
        );
    }
}


export default Radium(Block);