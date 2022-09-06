import { Routes, Route } from "react-router-dom";
import Signin from "./Pages/Login";
import Dashboard from "./Pages/Dashboard";
import Account from "./Pages/Account";

function App() {
  return (
    <>

      <Routes>
        <Route path="/login" element={<Signin/>}/>
        <Route path="/account" element={<Account/>}/>
        <Route path="/dashboard" element={<Dashboard/>}/>
      </Routes>
    </>
  );
}

export default App;
