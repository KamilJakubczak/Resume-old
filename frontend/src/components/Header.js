import React, { Component } from 'react';
import './Header.css';

class  Header extends Component{

    render(){
        return (
          <React.Fragment>
             <header className="masthead mb-auto">
                <div className="inner">
                    <div className="masthead-brand logo-wrap">
                        <h3 className=" logo">Kamil Jakubczak</h3>
                        <div className="logo line"></div>
                    </div>
                
                <nav className="nav nav-masthead justify-content-center">
                    <a  href="#contact">Projects</a>
                    <a  href="#">Experience</a>
                    <a  href="#">Education</a>
                    <a  href="#">Contact</a>
                </nav>
                </div>
            </header>
          </React.Fragment>
        )

    }
}

export default Header;