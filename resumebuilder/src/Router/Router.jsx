import React from 'react';
import { Routes, Route } from 'react-router-dom';

import Home from '../Pages/Home';
import Contact from '../Pages/Contact';
import Services from '../Pages/Services';
import About from '../Pages/About';

const Routers = () => {
    return (
        <Routes>
            <Route path="/" element={<Home/>} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/services" element={<Services />} />
        </Routes>
    );
};

export default Routers;
