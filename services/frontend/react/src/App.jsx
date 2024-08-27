import { useState } from 'react'
import { BrowserRouter, Route, Routes } from "react-router-dom";

import Navbar from "./components/Navbar.jsx";
import Footer from "./components/Footer.jsx";
import HomePage from "./views/HomePage/HomePage.jsx";
import ModelPage from "./views/ModelPage/ModelPage.jsx";
import DatasetPage from "./views/DatasetPage/DatasetPage.jsx";
import TrainPage from "./views/TrainPage/TrainPage.jsx";
import PredictionPage from "./views/PredictPage/PredictPage.jsx";

import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
        <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
            <Route path="/model" element={<ModelPage />} />
            <Route path="/dataset" element={<DatasetPage />} />
            <Route path="/train" element={<TrainPage />} />
            <Route path="/predict" element={<PredictionPage />} />
        </Routes>
            <Footer />
      </BrowserRouter>
    </>
  )
}

export default App
