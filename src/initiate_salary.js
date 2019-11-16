import React from "react";
import DatePicker from "react-datepicker";
import DayPicker, { DateUtils } from 'react-day-picker';
import 'react-day-picker/lib/style.css';

import "react-datepicker/dist/react-datepicker.css";
import axios from "axios";
import Background from "./images/wallpaper.jpg"
import MyNavbar from "./MyNavbar"
import Table from "react-bootstrap/Table"
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"

class initiate_salary extends React.Component {
    constructor(props) {
        super(props)
        this.state = {e_type:""}

        //alert("Update Calendar Page");
    }
handleSubmit = () => {
    //alert(this.state.dept_id);
    //alert(this.state.e_type);
    axios.post('http://localhost:5000/initiate-salary-process/'+this.state.e_type)
    .then(res=>{if(res.status==200)
                {
                  alert("Salary Process initiated");}

                else{
                  alert("Error");
                }
              }
      )
}
render (){
    return (
    <div style={{backgroundImage:"url(" + Background + ")", height:"100%",backgroundRepeat:'no-repeat',backgroundSize:'cover'}} >
    <MyNavbar> </MyNavbar>
    <div class="put_in_center">
    <div style={{paddingLeft:'2%',paddingRight:'2%',paddingTop:'2%',paddingBottom:'2%'}}>
    <h1 style={{justifyContent:'center',display:'flex',paddingTop:'2%',paddingBottom:'2%'}}> Initiate Salary </h1>
    <Form>
      <Form.Group controlId="exampleForm.ControlSelect1">
        <Form.Label>Department ID</Form.Label>
        <Form.Control id = "fc" as="select" onClick={(e) => {this.setState({e_type:e.target.value})}}>
        <option>DEV</option>
        <option>MANAGER</option>
        <option>HOD</option>
        <option>ACCOUNTANT</option>
        <option>HR</option>
        </Form.Control>
      </Form.Group>
    </Form>
    <Button onClick={this.handleSubmit} variant="secondary">Initiate Salary</Button>
    </div>
    </div>
    </div>
)
}
}
export default initiate_salary
