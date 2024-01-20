import logo from './logo.svg';
import './App.css';

function ent() {
  var x = document.getElementById("fname").value;
  document.getElementById("demo").innerHTML = x;
}

function App() {
  return (
    <div className="App">
      <body>
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>

        <div class="titlebx">
          <h1 class="title">Mrs. Info</h1>
        </div>

        <div class="wrapper">
          <div class="content" role="main">
          <div class="inbx">
            <input type="text" id="fname" name="fname" value="" placeholder="TikTok Link.."/><br />
            <button onclick={ent} >Enter</button>
          </div>
          <div class="outbx">
            <p class="outtxt" id="demo">hello this is the output area</p>
          </div>
          
          </div>
        </div>

        <footer class="footer">
      
        </footer>
      </body>
    </div>
  );
}

export default App;
