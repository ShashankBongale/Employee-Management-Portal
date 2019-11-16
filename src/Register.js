import React from "react"
import axios from "axios"
class Register extends React.Component{
    constructor(props){
        super(props)
        this.state={email:"",password:"",dept_id:"",stat:0}
        console.log("register page")
    }
    handleSubmit = (e) => {
        e.preventDefault()
        console.log(this.state.email,this.state.password)
        //axios.post("http://13.234.55.47:5000/register",{user_name:this.state.email,password:this.state.password,dept_id:this.state.dept_id})
        axios.post("http://localhost:5000/register",{user_name:this.state.email,password:this.state.password,dept_id:this.state.dept_id})
        .then(res=>{
            if(res.status==200)
            console.log("registered")
        }
            )
        this.props.history.push("/l")                           
      } 
    render(){
        return(
            <div>
                <p>Register page</p>
                <form onSubmit={this.handleSubmit}>
                        <div>                        
                            <label htmlFor="Username">Username</label>
                            <input type="text" placeholder="username enter that one" onChange={(e) => this.setState({email: e.target.value})}/>
                        </div>
                        <div>                        
                            <label htmlFor="Department">Department</label>
                            <input type="text" placeholder="department enter that one" onChange={(e) => this.setState({dept_id: e.target.value})}/>
                        </div>
                        <div>                        
                            <label htmlFor="password">Password</label>
                            <input type="password" onChange={(e) => this.setState({password: e.target.value})}/>
                        </div>
                        <input type="submit" value="Register" />
                </form>
            </div>
        )
        }
}
export default Register;