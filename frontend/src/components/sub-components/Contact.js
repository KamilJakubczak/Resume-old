import React, { Component } from 'react'
import './Contact.css'
class  Contact extends Component{

    state = {
        details: [],
    };

    componentDidMount(){
        fetch('http://127.0.0.1:8000/cv/positions/',{
            method: 'GET'
        }).then(resp => resp.json())
        .then(res => console.log(res))
        .catch(error => console.log(error))
     
    }
    
    render(){
        return (
          <React.Fragment>
           <div className="contact" id='contact'>
               <div className='content'>
                   Mail
               </div>
           </div>
          </React.Fragment>
        )

    }
}

export default Contact;