import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./Navbar";
import Home from "./Home";
import Register from "./Register";
import Allstudents from "./Allstudents";
import Update from "./Update";
import Delete from "./Delet";

function App() {
  return (
    <BrowserRouter>

      <Navbar />

      <Routes>

        <Route path="/" element={<Home />} />

        <Route path="/register" element={<Register />} />

        <Route path="/allstudents" element={<Allstudents />} />

        <Route path="/update" element={<Update />} />

        <Route path="/delete" element={<Delete />} />

      </Routes>

    </BrowserRouter>
  );
}

export default App;