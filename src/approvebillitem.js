import React from "react"
import Axios from "axios"
import { Redirect } from 'react-router-dom'
import MyNavbar from "./MyNavbar"
class ABillitem extends React.Component{
    constructor(props){
        super(props)
        var s=props.item.status
        console.log(s)
        this.state={status:s}
    }
    render(){
        return(
            <div>
                <div>
                    <p> Bill ID {this.props.item.bill_id +"  "} </p>
                    <img src={"data:image/jpeg;base64,"+this.props.item.bill_image} alt="bill_image"/>
                    <p> Status: {this.state.status+"  "} </p>
                     <p></p>
                </div>
            </div>
        )
    }
}
export default ABillitem
