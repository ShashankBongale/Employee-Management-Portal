import React from "react"
import axios from "axios"

class Salary extends React.Component{
    constructor(props){
        super(props)
        this.state={salary:0,bonus:0,bonus_status:false,salary_status:false}
        //event.preventDefault
        console.log("inside the salary page",props.eid)
        //axios.get('http://13.234.55.47:5000/display_salary/'+props.eid)
        axios.get('http://localhost:5000/display_salary/'+props.eid)
        .then(
           response=> {console.log(response.data)
           this.setState({salary:response.data.Salary})
           this.setState({bonus:response.data.bonus_amount})
           this.setState({bonus_status:response.data.bonus_status})
           this.setState({salary_status:response.data.salary_status})
        }
        );
    }
    render(){
        return(
            <div>
            <p>salary</p>
            <p> salary :{this.state.salary}</p>
            <p> bonus :{this.state.bonus}</p>
            <p> salary status :{this.state.salary_status}</p>
            <p> bonus status: {this.state.bonus_status}</p>
            </div>
        )
    }
}
export default Salary