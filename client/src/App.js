import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";

function ent() {
  var x = document.getElementById("fname").value;
  document.getElementById("demo").innerHTML = x;
}

function App() {

  const [urlString, setUrlString] = useState("a");

  return (
    <div className="App">
      <body>
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>

        <div className="titlebx">
          <h1 className="title">Mrs. Info</h1>
        </div>

        <div className="wrapper">
          <div className="content" role="main">
          <div className="inbx">
            <input type="text" onChange={(e) => setUrlString(e.target.value)} id="fname" name="fname" value={urlString} placeholder="TikTok Link.."/><br />
            <button onclick={ent} >Enter</button>
          </div>
          <div className="outbx">
            <p className="outtxt" id="demo">hello this is the output area</p>
          </div>
          
          </div>
        </div>

        <footer className="footer">
      
        </footer>
      </body>
    </div>
  );
}

export default App;
