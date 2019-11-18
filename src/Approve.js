import React from 'react';
import MyNavbar from "./MyNavbar"


class Approve extends React.Component {
    constructor(props){
        super(props)

    }
    render(){
        return (
        <div>
            <MyNavbar/>
            <h1>put approve stuff</h1>
            {console.log("inside the approve",this.props.eid)  }
            
        </div>
        );
    }
}

export default Approve;
