import React, { Component } from 'react';
import './Header.css';

class  Header extends Component{

    render(){
        return (
          <React.Fragment>
             <header>
                <nav className="nav navbar-expand-lg fixed-top">
                    <div className="logo-wrap">
                        <h3 className=" logo">Kamil Jakubczak</h3>
                        <div className="logo line"></div>
                    </div>
                    <div className="justify-content-end">
                    <a  href="#">Projects</a>
                    <a  href="#experience">Experience</a>
                    <a  href="#education">Education</a>
                    <a  href="#contact">Contact</a>
                    </div>
                </nav>
            </header>
          </React.Fragment>
        )

    }
}

export default Header;