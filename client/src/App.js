import logo from './logo.svg';
import './App.css';

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
          <form class="inbx">
            <input type="text" id="fname" name="fname" value="" placeholder="TikTok Link.."/><br />
            <input type="submit" value="Submit" />
          </form>
        
      </div>
      
      <div class="out">
        <form class="outbx">
            <output name="x" for=""></output>
        </form>
      </div>
    </div>
    <footer class="footer">
      <div class="links"></div>
      
    </footer>
  </body>
    </div>
  );
}

export default App;
