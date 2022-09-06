import { Routes, Route } from "react-router-dom";
import Signin from "./Pages/Signin";
import Dashboard from "./Pages/Dashboard";
import Account from "./Pages/Account";

function App() {
  return (
    <>

      <Routes>
        <Route path="/signin" element={<Signin/>}/>
        <Route path="/account" element={<Account/>}/>
        <Route path="/dashboard" element={<Dashboard/>}/>
      </Routes>
    </>
  );
}

export default App;
