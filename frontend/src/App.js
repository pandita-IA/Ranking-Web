import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Ranking from './components/Ranking';
import Usuarios from './components/Usuarios';


const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/ranking" element={<Ranking />} />
                <Route path="/usuarios" element={<Usuarios />} />
            </Routes>
        </Router>
    );
};

export default App;
