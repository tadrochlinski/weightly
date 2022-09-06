import { Routes, Route } from "react-router-dom";
import GlobalStyle from "./Components/GlobalStyles";
import Signin from "./Pages/Login/Login";
import Dashboard from "./Pages/Dashboard";
import Account from "./Pages/Account";

function App() {
  return (
    <>
      <GlobalStyle/>

      <Routes>
        <Route path="/login" element={<Signin/>}/>
        <Route path="/account" element={<Account/>}/>
        <Route path="/dashboard" element={<Dashboard/>}/>
      </Routes>
    </>
  );
}

export default App;
