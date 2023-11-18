import './App.css';
// hooks start with use
import { useState } from 'react'

function App() {
  //let name = 'Mario'
  const [name, setName] = useState('Mario')
  
  const handleClick = () => {
    //name = 'Luigi'
    setName('Luigi')
    console.log(name)
  }

  return (
    <div className="App">
      <h1>My name is {name}</h1>
      <button onClick = {handleClick}>Change name</button>
    </div>
  );
}

export default App;
