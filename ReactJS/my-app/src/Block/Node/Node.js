import React from 'react';
import './Node.css';

const Node = (props) => {
    return (
    <div className='Node'>
        <p>{props.text}</p>
        <input type='text' onChange={props.changed}/>
    </div>
    );
}

export default Node;