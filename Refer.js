import React from "react";
import axios from "axios";
import Background from "./images/wallpaper.jpg"
import MyNavbar from "./MyNavbar"
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import ReactFileReader from 'react-file-reader';

 // put drop down for method and change request

class Refer extends React.Component {
  constructor(props){
    super(props)
    this.handleFile = this.handleFile.bind(this);
    this.handleUpload = this.handleUpload.bind(this);
    
    this.state = {
      file: ""
    }
}

  handleFile(e){
    let f = e.target.files[0];
    var reader = new FileReader();

    reader.onload = function(event) {
      let con = event.target.result;
      this.setState({file: con})
    }.bind(this);

    reader.readAsText(f);
  }


  handleUpload(e){
    var resume_text = this.state.file
    axios.post('http://localhost:5000/nlp_engine',{input_string: resume_text})
        .then(res=>{
          if(res.status==200){
            alert("Recognised Domain: " + res.data[0])} 
          else{
            alert("Unable to classify !")}
              })
}


 
  render(){
    return (
      <div style={{backgroundImage:"url(" + Background + ")", height:"100%",backgroundRepeat:'no-repeat',backgroundSize:'cover'}} >
        <MyNavbar> </MyNavbar>
        <div class="put_in_center">
            <h2 style={{display:'flex',paddingTop:'2%',paddingBottom:'2%', justifyContent:'center'}}>Domains</h2>
  
            <ul style={{display:'flex', paddingLeft: '100px'}}>
            <li style={{display:'flex', paddingLeft: '50px', backgroundColor:"black", color:"white"}}><h5>Machine Learning</h5></li>
            <li style={{display:'flex', paddingLeft: '80px', backgroundColor:"black", color:"white"}}><h5>Web Technology</h5></li>
            <li style={{display:'flex', paddingLeft: '80px', backgroundColor:"black", color:"white"}}><h5>Computer Networks</h5></li>
            <li style={{display:'flex', paddingLeft: '80px', backgroundColor:"black", color:"white"}}><h5>Cloud Computing</h5></li>
            <li style={{display:'flex', paddingRight: '50px', paddingLeft: '80px', backgroundColor:"black", color:"white"}}><h5>Computer Graphics</h5></li>
            </ul>  
            <br></br>
            <br></br>
            <h2 style={{justifyContent:'center',display:'flex',paddingTop:'2%',paddingBottom:'2%'}}>Upload Resume</h2>
            
        <div class="pushtoright">
        <Form>
          <Form.Group controlId="exampleForm.ControlTextarea1">
            <input type="file" name="file" accept=".txt" onChange={(e)=>this.handleFile(e)} />
          </Form.Group>
        </Form>
        
        <Button style={{width:"580px"}} onClick={(e)=>this.handleUpload(e)} variant="secondary">Submit Resume</Button>
        </div>
        </div>
      </div>
    );
  }
}
export default Refer
