import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";


function App() {

  const [urlString, setUrlString] = useState("");
  const [infoString, setInfoString] = useState("");

  function handleClick(url) {
    setInfoString("your url: " + url)
  }

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
            <button onClick={() => handleClick(urlString)} >Enter</button>
          </div>
          <div className="outbx">
            <p className="outtxt" id="demo">{infoString}</p>
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
