import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";
import { TikTokEmbed } from 'react-social-media-embed';
import { RotatingLines } from "react-loader-spinner";

function Loader() {
  return(
    <RotatingLines
      strokeColor="grey"
      strokeWidth='5'
      animationDuration='0.75'
      width='50'
      visible={true}
    />
  )
}

function parseUrl(url) {
  let match = url.match(/https:\/\/www.tiktok.com\/@.+?\/video\/\d+/g)
  console.log(match)
  if (match)
    return match[0]
  else
    return ""
}

function App() {

  const [urlString, setUrlString] = useState("");

  const [infoString, setInfoString] = useState("");
  const [snopesString, setSnopesString] = useState("");

  const [loading, setLoading] = useState(false);

  function handleClick(url) {

    setLoading(true)

    fetch("http://localhost:5000/api/fact-check", {
      method: "POST",
      headers: {
      'Content-Type' : 'application/json'
      },
      body: JSON.stringify(url)
    })
    .then(res => res.json())
    .then(data => {
      setInfoString(data.summary)
      setSnopesString(data.snopes)
      setLoading(false)
    })
    .catch(err => console.log(err));
  }

  return (
    <div className="App">
      <head>
          <title>Miss Info</title>
      </head>
      <body>

        <div className="titlebx">
          <h1 className="title">Miss Info</h1>
        </div>

        <div className="wrapper">
          <div className="content" role="main">
          <div className="inbx">
            <input type="text" onChange={(e) => setUrlString(e.target.value)} id="fname" name="fname" value={urlString} placeholder="TikTok Link.."/><br />
            <button onClick={() => handleClick(urlString)} >{loading ? "Loading..." : "Enter"}</button>
          </div>
          <div style={{ display: 'flex', justifyContent: 'center', display: parseUrl(urlString) == "" ? 'none' : '' }}>
            <TikTokEmbed url={parseUrl(urlString)} width={325} />
          </div>
          <div className="outbx" style={{display: infoString == "" ? "none" : ""}}>
            {loading ? <Loader/> : <p className="outtxt" id="demo">{infoString}</p>}
          </div>
          <div className="outbx" style={{display: snopesString == "" ? "none" : ""}}>
            <p className="outtxt">{snopesString}</p>
          </div>
          
          </div>
        </div>
      </body>
    </div>
  );
}

export default App;
