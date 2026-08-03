import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import History from "./pages/History";
import Patients from "./pages/Patients";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/history" element={<History />} />
                <Route path="/patients" element={<Patients/>} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
