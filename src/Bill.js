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
import {Link} from "react-router-dom"

class Bill extends React.Component {
    constructor(props){
        super(props)
        this.state = {rem:"",bill_image:"",bill_amount:""}
        this.imgb64 = "";
        axios.get('http://127.0.0.1:5000/bill_rem/'+props.eid)
        .then(res=>{
            this.setState({rem:res.data.rem})
        })
    }
    handleChange_image = () => {
        var doc = document;
         var form = doc.getElementById("img");
         var file = form.files[0];
         var reader = new FileReader();
         var imgb64;
         reader.onloadend = function() {
           var t = reader.result;
       		var img = t.split(/,(.+)/)[1];
            var dom = document.getElementById("p");
            dom.innerHTML = img;
         }
         reader.readAsDataURL(file);
    }
    handleSubmit = (e) => {
        alert(this.state.bill_amount)
        //alert(this.state.bill_image)
        var dom = document.getElementById("p");
        //alert(dom.innerHTML);
        var imgb64 = dom.innerHTML;
        axios.post('http://127.0.0.1:5000/apply_bill',{"e_id":this.props.eid,"bill_image":imgb64,"bill_amount":this.state.bill_amount})
        .then(res=>{if(res.status==200){alert("Application Submitted");
                                  }
                      if(res.status==400){
                          alert("No sufficient funds")}

                  })
              }
render()
{
    return (
        <html>
        <head>
        <title> Bill </title>
        </head>
        <body style={{backgroundImage:"url(" + Background + ")",backgroundSize:"cover",backgroundPosition:"center",backgroundRepeat:"no-repeat"}}>
        <MyNavbar> </MyNavbar>
        <div class="put_in_center" stype={{marginBottom:'25%'}}>
        <h2 style={{justifyContent:'center',display:'flex',paddingTop:'2%',paddingBottom:'2%'}}>Bills</h2>
        <Table striped bordered hover style={{width:'80%',marginLeft:'10%'}}>
          <thead>
            <tr>
              <th style={{justifyContent:'center',display:'flex'}}>Reimbursable Amount Remaining For This Month</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><p style={{justifyContent:'center',display:'flex'}}>{this.state.rem}</p></td>
            </tr>
          </tbody>
        </Table>
        <h2 style={{justifyContent:'center',display:'flex',paddingTop:'2%',paddingBottom:'2%'}}>Apply For New Bills</h2>
        <div style={{marginLeft:"25%",marginRight:"25%"}}>
        <Form>
        <Form.Group controlId="exampleForm.ControlText1">
          <Form.Label>Bill Amount</Form.Label>
          <Form.Control type="text" onChange={(e) => {this.setState({bill_amount:e.target.value})}} />
          </Form.Group>
            <Form.Group controlId="exampleForm.ControlImage">
            <Form.Label> Bill Image </Form.Label>
            <Form.Control type="file" onChange={this.handleChange_image} id="img"/>
            </Form.Group>
            </Form>
            <div style={{marginTop:"5%"}}>
            <Button onClick={this.handleSubmit} variant="secondary">Submit Leave application</Button>
            <Button variant="secondary" style={{marginLeft:"24%"}} ><Link to="/view_bills" style={{color:'white'}}>View Bill Application</Link></Button>
            </div>
            </div>
            <p id = "p" hidden>hhh </p>
        </div>
        </body>
        </html>
        )
    }
}
export default Bill
