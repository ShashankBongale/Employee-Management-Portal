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

 // put drop down for method and change request

class Leave extends React.Component {
  constructor(props){
    super(props)
    this.handleDayClick = this.handleDayClick.bind(this);
    this.state = {selectedDays:[],reason:"",reason_category:"",resp:"",casual:"",earned:"",medical:""}
    //axios.get('http://13.234.55.47:5000/get_leave_data/'+props.eid)
    axios.get('http://localhost:5000/get_leave_data/'+props.eid)
    .then(res=>{
                console.log(res.data)
                this.setState({casual:res.data.casual})
                this.setState({earned:res.data.earned})
                this.setState({medical:res.data.medical})
                console.log(this.state)
              })
}

  handleDayClick = (day, { selected }) => {
    const { selectedDays } = this.state;
    if (selected) {
      const selectedIndex = selectedDays.findIndex(selectedDay =>
        DateUtils.isSameDay(selectedDay, day)
      );
      selectedDays.splice(selectedIndex, 1);
    } else {
      selectedDays.push(day);
    }
    this.setState({ selectedDays });
  }

  handleSubmit = () => {
    console.log(this.state.reason)
    let selectedDays = this.state.selectedDays
    console.log(this.state.reason_category)
    console.log(this.props.eid)
    //axios.post('http://13.234.55.47:5000/apply_leave',{"e_id":this.props.eid,"type":"medical","list_of_dates":datearray,"reason":this.state.reason,"status":"pending"})
    axios.post('http://localhost:5000/apply_leave',{"e_id":this.props.eid,"type":"medical","list_of_dates":selectedDays,"reason":this.state.reason,"status":"pending"})
    .then(res=>{if(res.status===200)
                {
                  alert("Leave application submitted")}
                else{
                  alert("Enter valid details")
                }
              }
      )
    
    //console.log(resp)
  }

  handleStatusCheck = () => {
    axios.get('http://loaclhost:5000/get_leave_status'+this.props.eid)
    .then(res=>{
      alert(res)
    })
  }

 
  render(){
    return (
      <div style={{backgroundImage:"url(" + Background + ")", height:"100%",backgroundRepeat:'no-repeat',backgroundSize:'cover'}} >
        <MyNavbar> </MyNavbar>
        <div class="put_in_center">
            <h2 style={{justifyContent:'center',display:'flex',paddingTop:'2%',paddingBottom:'2%'}}>Personal Leave Details</h2>
  
            <Table striped bordered hover style={{width:'80%',marginLeft:'10%'}}>
              <thead>
                <tr>
                  <th>Casual</th>
                  <th>Medical</th>
                  <th>Earned</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><p>{this.state.casual}</p></td>
                  <td><p>{this.state.medical}</p></td>
                  <td><p>{this.state.earned}</p></td>
                </tr>
              </tbody>
            </Table>

            <h2 style={{justifyContent:'center',display:'flex',paddingTop:'2%',paddingBottom:'2%'}}>Apply Leave</h2>
            <DayPicker style={{backgroundColor:'azure'}}
              selectedDays={this.state.selectedDays}
              onDayClick={this.handleDayClick}
            />
        <div class="pushtoright">
        <Form>
          <Form.Group controlId="exampleForm.ControlSelect1">
            <Form.Label>Type of Leave</Form.Label>
            <Form.Control as="select" onChange={(e) => {this.setState({reason_category:e.target.value})
                          console.log(this.state.reason_category)
                        }
                  }>
              <option>Casual</option>
              <option>Medical</option>
              <option>Earned</option>
            </Form.Control>
          </Form.Group>
          <Form.Group controlId="exampleForm.ControlTextarea1">
            <Form.Label>Reason</Form.Label>
            <Form.Control as="textarea" rows="2" onChange={(e) => {this.setState({reason:e.target.value})
                          console.log(this.state.reason)
                        }
                  }/>
          </Form.Group>
        </Form>
        
        <Button onClick={this.handleSubmit} variant="secondary">Submit Leave application</Button>
        </div>
        <Button onClick={this.handleStatusCheck} style={{float:'right',marginBottom:'1%',marginRight:'1%'}} variant="info">Check Leave Application Status</Button>
        </div>
      </div>
    );
  }
}
export default Leave