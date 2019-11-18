import React from "react";

import axios from "axios";
import MyNavbar from "./MyNavbar"
import Background from "./images/traffic.jpg"
import Table from "react-bootstrap/Table"
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import ButtonToolbar from "react-bootstrap/ButtonToolbar"
import Nav from 'react-bootstrap/Nav'
import Tab from 'react-bootstrap/Tab'
import Tabs from 'react-bootstrap/Tabs'
import DropdownButton from 'react-bootstrap/DropdownButton'
import Dropdown from 'react-bootstrap/Dropdown'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

class Cab extends React.Component {
    constructor(props){
        super(props)
        this.state = {login_time:0,logout_time:0,c_type:""}
    }

    setLoginTime = (evtKey, evt) => {
        this.setState({login_time:evtKey})
        document.getElementById("in").innerHTML = evtKey + " AM"
    }

    setLogoutTime = (evtKey, evt) => {
        this.setState({logout_time:evtKey})
        document.getElementById("out").innerHTML = (evtKey - 12) + " PM"
    }

    bookLogin = () => {
        if(this.state.login_time != 0){
            axios.post('http://localhost:5000/book_login',{"e_id":this.props.eid,"login":this.state.login_time})
            .then(res=>{if(res.status===200)
                        {
                            alert("Cab booked successfully.")
                            document.getElementById("loginSubmit").innerHTML = "Booked"
                            document.getElementById("loginSubmit").style.backgroundColor = "#5CB85C"
                            setTimeout(function() { //Start the timer
                                document.getElementById("loginSubmit").innerHTML = "Book cab"
                                document.getElementById("loginSubmit").style.backgroundColor = "red" //After 1 second, set render to true
                            }.bind(this), 1500)
                        }
                        else{
                        alert("Error while booking")
                        }
                    }
            )
        }
        else{
            alert("Please choose your login time!.")
        }
        this.setState({login_time:0})
    }

    bookLogout = () => {
        if(this.state.logout_time != 0){
            axios.post('http://localhost:5000/book_logout',{"e_id":this.props.eid,"logout":this.state.logout_time})
            .then(res=>{if(res.status===200)
                        {
                            alert("Cab booked successfully.")
                            document.getElementById("logoutSubmit").innerHTML = "Booked"
                            document.getElementById("logoutSubmit").style.backgroundColor = "#5CB85C"
                            setTimeout(function() { //Start the timer
                                document.getElementById("logoutSubmit").innerHTML = "Book cab"
                                document.getElementById("logoutSubmit").style.backgroundColor = "red" //After 1 second, set render to true
                            }.bind(this), 1500)
                        }
                        else{
                        alert("Error while booking")
                        }
                    }
            )
        }
        else{
            alert("Please choose your logout time!.")
        }
        this.setState({logout_time:0})
    }

    setCommuteType = (eventKey,evt) => {
        this.setState({c_type:eventKey})
        document.getElementById("ctype").innerHTML = eventKey
    }

    cancelCab = () => {
        if(this.state.c_type != ""){
            if(this.state.c_type == "Login"){
                axios.post('http://localhost:5000/cancel_login',{"e_id":this.props.eid})
                .then(res=>{if(res.status===200)
                    {
                        alert("Cab cancelled successfully.")
                        document.getElementById("cancelCab").innerHTML = "Cancelled"
                        document.getElementById("cancelCab").style.backgroundColor = "#5CB85C"
                        setTimeout(function() { //Start the timer
                            document.getElementById("cancelCab").innerHTML = "Cancel cab"
                            document.getElementById("cancelCab").style.backgroundColor = "red" //After 1 second, set render to true
                        }.bind(this), 1500)
                    }
                    else{
                    alert("Error while cancelling")
                    }
                }
                )
            }
            else{
                axios.post('http://localhost:5000/cancel_logout',{"e_id":this.props.eid})
                .then(res=>{if(res.status===200)
                    {
                        alert("Cab cancelled successfully.")
                        document.getElementById("cancelCab").innerHTML = "Cancelled"
                        document.getElementById("cancelCab").style.backgroundColor = "#5CB85C"
                        setTimeout(function() { //Start the timer
                            document.getElementById("cancelCab").innerHTML = "Cancel cab"
                            document.getElementById("cancelCab").style.backgroundColor = "red" //After 1 second, set render to true
                        }.bind(this), 1500)
                    }
                    else{
                    alert("Error while cancelling")
                    }
                }
                )
            }   
        }
        else{
            alert("Please choose your commute type!.")
        }
        this.setState({c_type:""})
    }

    getLoginInfo = () => {
        axios.post('http://localhost:5000/show_cab_details_login',{"e_id":this.props.eid})
        .then(res=>{
            // console.log(res.status)
            if(res.data.status != 400){
                // console.log(res.data)
                this.setState({cab_no:res.data.cab_number})
                this.setState({driver_name:res.data.driver_name})
                this.setState({driver_no:res.data.driver_number})
                console.log(this.state)
                // document.getElementById("loginTime").innerHTML = "Login time : " + this.state.login_time
                document.getElementById("inCabNo").innerHTML = "Cab number : " + this.state.cab_no
                document.getElementById("inDriverName").innerHTML = "Driver name : " + this.state.driver_name
                document.getElementById("inDriverNo").innerHTML = "Driver number : " + this.state.driver_no
                document.getElementById("inNot").innerHTML = ""
            }
            else{
                // console.log("noooooooooooo")
                document.getElementById("inCabNo").innerHTML = ""
                document.getElementById("inDriverName").innerHTML = ""
                document.getElementById("inDriverNo").innerHTML = ""
                document.getElementById("inNot").innerHTML = "Your cab has not been assigned yet!."
            }
                
              })

        axios.post('http://localhost:5000/show_cab_details_logout',{"e_id":this.props.eid})
        .then(res=>{
            // console.log(res.status)
            if(res.data.status != 400){
                // console.log(res.data)
                this.setState({cab_no:res.data.cab_number})
                this.setState({driver_name:res.data.driver_name})
                this.setState({driver_no:res.data.driver_number})
                console.log(this.state)
                // document.getElementById("loginTime").innerHTML = "Login time : " + this.state.login_time
                document.getElementById("outCabNo").innerHTML = "Cab number : " + this.state.cab_no
                document.getElementById("outDriverName").innerHTML = "Driver name : " + this.state.driver_name
                document.getElementById("outDriverNo").innerHTML = "Driver number : " + this.state.driver_no
                document.getElementById("outNot").innerHTML = ""
            }
            else{
                // console.log("noooooooooooo")
                document.getElementById("outCabNo").innerHTML = ""
                document.getElementById("outDriverName").innerHTML = ""
                document.getElementById("outDriverNo").innerHTML = ""
                document.getElementById("outNot").innerHTML = "Your cab has not been assigned yet!."
            }
                
            })
    }


    render() {
        return (
            <div style={{backgroundImage:"url(" + Background + ")"}}>
                <MyNavbar> </MyNavbar>
                <div style={{backgroundColor:'#F8F8F8',padding:'0 10% 0 10%',margin:'4% 10% 4% 10%',alignItems:'center',border:'2px solid #008ae6',height:'75%'}}>
                <Tab.Container id="left-tabs-example" defaultActiveKey="book">
                    <Nav variant="pills" className="justify-content-center">
                        <Nav.Item style={{margin:'2%'}}>
                            <Nav.Link eventKey="book">Book Cab</Nav.Link>
                        </Nav.Item>
                        <Nav.Item style={{margin:'2%'}}>
                            <Nav.Link eventKey="info" onClick={this.getLoginInfo}>Cab Information</Nav.Link>
                        </Nav.Item>
                        <Nav.Item style={{margin:'2%'}}>
                            <Nav.Link eventKey="cancel">Cancel cab</Nav.Link>
                        </Nav.Item>
                    </Nav>
                    <Tab.Content>
                        <Tab.Pane eventKey="book">
                            <Tabs defaultActiveKey="login" id="uncontrolled-tab-example">
                                <Tab eventKey="login" title="Login">
                                    <div style={{padding:'5%',margin:'3%'}}>
                                    <Row>
                                        <Col>
                                        <DropdownButton style={{marginLeft:'45%'}} id="dropdown-basic-button" title="Select login time" onSelect={this.setLoginTime}>
                                            <Dropdown.Item eventKey='5'>5 AM</Dropdown.Item>
                                            <Dropdown.Item eventKey='8'>8 AM</Dropdown.Item>
                                            <Dropdown.Item eventKey='11'>11 AM</Dropdown.Item>
                                        </DropdownButton>
                                        </Col>
                                        <Col>
                                        <h1 id="in">NIL</h1>
                                        </Col>
                                    </Row>
                                    <Button style={{marginLeft:'42%',marginTop:'14%'}} variant="danger" onClick={this.bookLogin} id="loginSubmit">Book Cab</Button>
                                    </div>
                                </Tab>
                                <Tab eventKey="logout" title="Logout">
                                    <div style={{padding:'5%',margin:'3%'}}>
                                    <Row>
                                        <Col>
                                        <DropdownButton style={{marginLeft:'45%'}} id="dropdown-basic-button" title="Select logout time" onSelect={this.setLogoutTime}>
                                            <Dropdown.Item eventKey='15'>3 PM</Dropdown.Item>
                                            <Dropdown.Item eventKey='18'>6 PM</Dropdown.Item>
                                            <Dropdown.Item eventKey='21'>9 PM</Dropdown.Item>
                                        </DropdownButton>
                                        </Col>
                                        <Col>
                                        <h1 id="out">NIL</h1>
                                        </Col>
                                    </Row>
                                    <Button style={{marginLeft:'42%',marginTop:'14%'}} variant="danger" onClick={this.bookLogout} id="logoutSubmit">Book Cab</Button>
                                    </div>
                                </Tab>
                            </Tabs>
                        </Tab.Pane>
                        <Tab.Pane eventKey="info">
                            <Tabs defaultActiveKey="login" id="uncontrolled-tab-example">
                                <Tab onClick={this.getLoginInfo} eventKey="login" title="Login">
                                    <div style={{marginTop:'5%',marginLeft:'15%'}}>
                                        <h1 id="loginTime"></h1>
                                        <h1 id="inCabNo"></h1>
                                        <h1 id="inDriverName"></h1>
                                        <h1 id="inDriverNo"></h1>
                                        <h1 id="inNot"></h1>
                                    </div>
                                </Tab>
                                <Tab onClick={this.getLoginInfo} eventKey="logout" title="Logout">
                                    <div style={{marginTop:'5%',marginLeft:'15%'}}>
                                        <h1 id="logoutTime"></h1>
                                        <h1 id="outCabNo"></h1>
                                        <h1 id="outDriverName"></h1>
                                        <h1 id="outDriverNo"></h1>
                                        <h1 id="outNot"></h1>
                                    </div>
                                </Tab>
                            </Tabs>
                        </Tab.Pane>
                        <Tab.Pane eventKey="cancel">
                            <div style={{margin:'5%',marginTop:'10%'}}>
                            <Row>
                                <Col>
                                <DropdownButton style={{marginBottom:'40%',marginLeft:'55%'}} id="dropdown-basic-button" title="Select commute type" onSelect={this.setCommuteType}>
                                    <Dropdown.Item eventKey='Login'>Login</Dropdown.Item>
                                    <Dropdown.Item eventKey='Logout'>Logout</Dropdown.Item>
                                </DropdownButton>
                                </Col>
                                <Col>
                                <h1 style={{marginLeft:'5%'}} id="ctype">NIL</h1>
                                </Col>
                            </Row>
                            <Button style={{marginLeft:'45%'}} variant="danger" onClick={this.cancelCab} id="cancelCab">Cancel Cab</Button>
                            </div>
                        </Tab.Pane>
                    </Tab.Content>
                </Tab.Container>    
                </div>
            </div>
        );
      }
}

export default Cab