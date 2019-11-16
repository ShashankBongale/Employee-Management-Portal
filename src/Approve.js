import React from 'react';
import MyNavbar from "./MyNavbar"
import axios from "axios"
import Leaveitem from "./Leaveitem"
import Tab from "react-bootstrap/Tab"
import Nav from "react-bootstrap/Nav"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"
import Background from "./images/wallpaper.jpg"

class Approve extends React.Component {
    constructor(props){
        super(props)
        this.state={items:[]}
        //axios.get("http://13.234.55.47:5000/get_leave_applications/"+this.props.eid)
        axios.get("http://localhost:5000/get_leave_applications/"+this.props.eid)
        .then(res=>{
                        const values=res.data
                        console.log("values are",values)
                        this.setState({items:values})
                    }
                )


    }
    handleChange(eid,resp){

    }
    render(){

        console.log("items are",this.state.items)
        const approveitems=this.state.items.map(item=><Leaveitem key={item.eid} item={item} handleChange={this.handleChange} />)
        return (
        <div style={{backgroundImage:"url(" + Background + ")", height:"100%",backgroundRepeat:'no-repeat',backgroundSize:'cover'}} >
            <MyNavbar/>
            <div class="put_in_center">
            <div style={{paddingLeft:'2%',paddingRight:'2%',paddingTop:'2%',paddingBottom:'2%'}}>
            <Tab.Container id="left-tabs-example" defaultActiveKey="first">
            <Row>
                <Col sm={3}>
                <Nav variant="pills" className="flex-column">
                    <Nav.Item>
                    <Nav.Link eventKey="first">Approve Leave Applications</Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                    <Nav.Link eventKey="second">Grant Bonus</Nav.Link>
                    </Nav.Item>
                </Nav>
                </Col>
                <Col sm={9}>
                <Tab.Content>
                    <Tab.Pane eventKey="first">
                    {approveitems}
                    </Tab.Pane>
                    <Tab.Pane eventKey="second">
                    <p>grant bonus comes here</p>
                    </Tab.Pane>
                </Tab.Content>
                </Col>
            </Row>
            </Tab.Container>

        </div>
        </div>
        </div>
        );
    }
}

export default Approve;
