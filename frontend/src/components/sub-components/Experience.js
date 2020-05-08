import React, { Component } from 'react'
import './Timeline.css'

import { VerticalTimeline, VerticalTimelineElement }  from 'react-vertical-timeline-component';
import 'react-vertical-timeline-component/style.min.css';
class  Experience extends Component{

    state = {
        details: [],
    };

    componentDidMount(){
        fetch('http://127.0.0.1:8000/cv/positions/',{
            method: 'GET'
        }).then(resp => resp.json())
        .then(res => this.setState({details:res}))
        .catch(error => console.log(error))
     
    }
    render(){
      return (
        <VerticalTimeline
        lineColor={'#ddd'}
        >
        {this.state.details.map(detail => { 
          return (
            <VerticalTimelineElement
            className="vertical-timeline-element--work"
            lineColor={{background: 'linear-gradient(to top, #03a9f4, #f441a5,#ffeb3b, #03a9f4)'}}
            date={detail.start_date}
            iconStyle={{ background: 'rgb(33, 150, 243)', color: '#fff' }}
            // icon={<WorkIcon />}
          >
            <h3 className="vertical-timeline-element-title">{detail.company}</h3>
            <h4 className="vertical-timeline-element-subtitle">{detail.position_title}</h4>
            <p className="vertical-timeline-element-description">{detail.description}</p>
          </VerticalTimelineElement>
          )
        })}
        </VerticalTimeline>

      )
    }
}

export default Experience;