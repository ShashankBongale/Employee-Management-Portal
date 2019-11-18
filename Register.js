import React from "react";
import DayPicker, { DateUtils } from 'react-day-picker';
import 'react-day-picker/lib/style.css';
 
import "react-datepicker/dist/react-datepicker.css";
import axios from "axios";
import Background from "./images/wallpaper.jpg"
import MyNavbar from "./MyNavbar"
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"

 // put drop down for method and change request

class Register extends React.Component {
  constructor(props){
    super(props)
    this.state = {user_name:"",password:"",dept_id:"",e_contact:"",e_email:"",e_type:"",approver_id:""}
}

  handleSubmit = () => {
    console.log(this.state.user_name)
    console.log(this.state.e_type)
    axios.post('http://localhost:5000/register', {"user_name":this.state.user_name,"password":this.state.password,"dept_id":this.state.dept_id,"e_contact":this.state.e_contact,"e_email":this.state.e_email, "e_type":this.state.e_type, "approver_id":this.state.approver_id})
    .then(res=>{if(res.status===200)
                {
                  alert("Employee Registered")}
                else{
                  alert("Recheck Entered Values")
                }
              }
      )
    
    //console.log(resp)
  }

 
  render(){
    return (
      <div style={{backgroundImage:"url(" + Background + ")", height:"100%",backgroundRepeat:'no-repeat',backgroundSize:'cover'}} >
        <MyNavbar> </MyNavbar>
        <div class="put_in_center">

            <h2 style={{justifyContent:'center',display:'flex',paddingTop:'2%',paddingBottom:'2%'}}>Enter Employee Detail</h2>
            
        <div class="pushtoright">
        <Form>
          <Form.Group controlId="exampleForm.ControlSelect1">
            <Form.Label>Employee Name &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;    </Form.Label>
            <Form.Control type="text" onChange={(e) => {this.setState({user_name: e.target.value})}} />
          </Form.Group>

          <Form.Group controlId="exampleForm.ControlSelect1">
            <Form.Label>Password &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</Form.Label>
            <Form.Control type="text" onChange={(e) => {this.setState({password: e.target.value})}} />
            <br></br>
          </Form.Group>

          <Form.Group controlId="exampleForm.ControlSelect1">
            <Form.Label>Department Id &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</Form.Label>
            <Form.Control type="text" onChange={(e) => {this.setState({dept_id: e.target.value})}} />
          </Form.Group>

          <Form.Group controlId="exampleForm.ControlSelect1">
            <Form.Label>Enter Contact Number &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; </Form.Label>
            <Form.Control type="text" onChange={(e) => {this.setState({e_contact: e.target.value})}} />
          </Form.Group>

          <Form.Group controlId="exampleForm.ControlSelect1">  
            <Form.Label>Enter Email Id &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</Form.Label>
            <Form.Control type="text" onChange={(e) => {this.setState({e_email: e.target.value})}} />
          </Form.Group>

          <Form.Group controlId="exampleForm.ControlSelect1">
            <Form.Label>Enter Employee Type &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</Form.Label>
            <Form.Control type="text" onChange={(e) => {this.setState({e_type: e.target.value})}} />
          </Form.Group>

          <Form.Group controlId="exampleForm.ControlSelect1">
            <Form.Label>Enter Approver Id &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;</Form.Label>
            <Form.Control type="text" onChange={(e) => {this.setState({approver_id: e.target.value})}} />
          </Form.Group>
        </Form>
        
        <Button onClick={this.handleSubmit} variant="secondary">Register Employee</Button>
        </div>
      </div>
    </div>
    );
  }
}
export default Register;
