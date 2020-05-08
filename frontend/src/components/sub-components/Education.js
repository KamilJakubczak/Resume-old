import React, { Component } from 'react'
import './Timeline.css'

import { VerticalTimeline, VerticalTimelineElement }  from 'react-vertical-timeline-component';
import 'react-vertical-timeline-component/style.min.css';
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
        <VerticalTimeline>
        {this.state.details.map(detail => { 
          return (
            <VerticalTimelineElement
            className="vertical-timeline-element--work"
            date={detail.start_date}
            iconStyle={{ background: 'rgb(33, 150, 243)', color: '#fff' }}
            icon={<img src={detail.school_logo} width="52" height="52"/>}
          >
            <h3 className="vertical-timeline-element-title">{detail.school_name}</h3>
            <h4 className="vertical-timeline-element-subtitle">{detail.course_name}</h4>
            <p className="vertical-timeline-element-description">{detail.description}</p>
          </VerticalTimelineElement>
          )
        })}
        </VerticalTimeline>

      )
    }
}

export default Education;