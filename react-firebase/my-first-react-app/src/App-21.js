import './App.css';
// hooks start with use
import { useState } from 'react'

function App() {
  //let name = 'Mario'
  const [name, setName] = useState('Mario')

  // Each object is a single event
  const [events, setEvents] = useState([
    {title: "Mario's birthday bash", id: 1},
    {title: "Bowser's live stream", id: 2},
    {title: "Race on Moo Moo Farm", id: 3}
  ])
  
  const handleClick = () => {
    //name = 'Luigi'
    setName('Luigi')
    
    console.log(name)
  }

  return (
    <div className="App">
      <h1>My name is {name}</h1>
      <button onClick = {handleClick}>Change name</button>

      { events.map((event, index) => (
        <div key={event.id}>
          <h2>{index} - {event.title}</h2>
        </div>
      )) }
    </div>
  );
}

export default App;
