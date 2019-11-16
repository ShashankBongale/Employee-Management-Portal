import React from "react"
import { Link } from 'react-router-dom';
import Navbar from "react-bootstrap/Navbar"
import Nav from "react-bootstrap/Nav"
import {ImageBackground} from  "react"
const Background_Image = () => {
    return (
        <ImageBackground source={require('./images/wallpaper.jpg')} style={{width:'100%',height:'100%'}}>
        </ImageBackground>
    );
}
export default Background_Image
