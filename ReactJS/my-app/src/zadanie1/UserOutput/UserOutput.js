import React, {Component} from 'react';

const userOutput = (props) => {
    return (
        <div>
            <p>Username:</p>
            <p>{props.username}</p>
        </div>
    )
}

export default userOutput;