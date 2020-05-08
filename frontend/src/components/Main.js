import React, { Component } from 'react'
import Contact from './sub-components/Contact';
import Experience from './sub-components/Experience';
import Education from './sub-components/Education';
class  Main extends Component{

    render(){
        return (
          <React.Fragment>
            <main role="main" className="inner cover">
              <div className="main">
                <Experience/>
                <Education/>
                <Contact/>
              </div>
            </main>    
          </React.Fragment>
        )

    }
}

export default Main;