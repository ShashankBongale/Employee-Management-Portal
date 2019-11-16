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

class update_calendar extends React.Component {
    constructor(props) {
        super(props)
        this.state = {dept_id:"",e_type:"",resp:"",casual:"",earned:"",medical:""}

        //alert("Update Calendar Page");
    }
handleSubmit = () => {
    //alert(this.state.dept_id);
    //alert(this.state.e_type);
    axios.post('http://localhost:5000/update_calendar',{dept_id:this.state.dept_id,e_type:this.state.e_type,medical:this.state.medical,earned:this.state.earned,casual:this.state.casual})
    .then(res=>{if(res.status===200)
                {
                  alert("Calendar Updated");}

                else{
                  alert("Error while updating");
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
    <h1 style={{justifyContent:'center',display:'flex',paddingTop:'2%',paddingBottom:'2%'}}> Update Calendar </h1>
    <Form>
      <Form.Group controlId="exampleForm.ControlSelect1">
        <Form.Label>Department ID</Form.Label>
        <Form.Control as="select" onClick={(e) => {this.setState({dept_id:e.target.value})}}>
          <option>DEVBNG</option>
          <option>FINDEP</option>
          <option>HRDEPT</option>
        </Form.Control>
      </Form.Group>
      <Form.Group controlId="exampleForm.ControlSelect2">
        <Form.Label>Employee Type</Form.Label>
        <Form.Control as="select" onClick={(e) => {this.setState({e_type:e.target.value})}}>
          <option>DEV</option>
          <option>MANAGER</option>
          <option>HOD</option>
          <option>ACCOUNTANT</option>
          <option>HR</option>
        </Form.Control>
      </Form.Group>
      <Form.Group controlId="exampleForm.ControlText1">
        <Form.Label>Casual</Form.Label>
        <Form.Control type="text" onChange={(e) => {this.setState({casual:e.target.value})
                      console.log(this.state.reason)
                    }
              }/>
      </Form.Group>
      <Form.Group controlId="exampleForm.ControlText2">
        <Form.Label>Earned</Form.Label>
        <Form.Control type="text" onChange={(e) => {this.setState({earned:e.target.value})
                      console.log(this.state.reason)
                    }
              }/>
      </Form.Group>
      <Form.Group controlId="exampleForm.ControlText3">
        <Form.Label>Medical</Form.Label>
        <Form.Control type="text" onChange={(e) => {this.setState({medical:e.target.value})
                      console.log(this.state.reason)
                    }
              }/>
      </Form.Group>
    </Form>
    <Button onClick={this.handleSubmit} variant="secondary">Update Calendar</Button>
    </div>
    </div>
    </div>
)
}
}
export default update_calendar
