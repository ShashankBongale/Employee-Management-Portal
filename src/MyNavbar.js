import React from "react"
import { Link } from 'react-router-dom';
import Navbar from "react-bootstrap/Navbar"
import Nav from "react-bootstrap/Nav"
const MyNavbar = () => {
    return(

        <Navbar bg="dark" variant="dark">
        <Navbar.Brand>EMS</Navbar.Brand>
        <Nav className="mr-auto">
          <Nav.Link><Link to="/App" style={{color:'white'}}>Home</Link></Nav.Link>
          <Nav.Link><Link to="/Leave" style={{color:'white'}}>Leave</Link></Nav.Link>
          <Nav.Link><Link to="/Salary" style={{color:'white'}}>Salary</Link></Nav.Link>
          <Nav.Link><Link to="/Bill" style={{color:'white'}}>Bill-Rimburse</Link></Nav.Link>
          <Nav.Link><Link to="/update_calendar" style={{color:'white'}}>Update Calendar</Link></Nav.Link>
          <Nav.Link><Link to="/initiate_salary" style={{color:'white'}}>Initiate Salary</Link></Nav.Link>
          <Nav.Link><Link to="/approve_bill" style={{color:'white'}}>Approve</Link></Nav.Link>
          <Nav.Link><Link to="/Cab" style={{color:'white'}}>Book-Cab</Link></Nav.Link>
        </Nav>
      </Navbar>
    );
}


export default MyNavbar
