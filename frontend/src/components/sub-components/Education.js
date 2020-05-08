import React, { Component } from 'react'
import './Education.css'

class  Education extends Component{

    state = {
        details: [],
    };

    componentDidMount(){
        fetch('http://127.0.0.1:8000/cv/educations/',{
            method: 'GET'
        }).then(resp => resp.json())
        .then(res => this.setState({details:res}))
        .catch(error => console.log(error))
     
    }
    render(){
      return (
          <div id="education" className="education-container">
        {this.state.details.map(detail => { 
          return (
           <div id="id-{detail.order}" className="box">
             <div className="content-box">
              <h2>{detail.school_name}</h2>
              <h4>{detail.course_name}</h4>
              <p>{detail.description}</p>

             </div>
           </div>
          )
        })}
        </div>
      )
    }
}

export default Education;