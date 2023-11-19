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

  }

  /* Currently at 0:54 */

  return (
    <div className="App">
      { events.map((event, index) => (
        <div key={event.id}>
          <h2>{index} - {event.title}</h2>
          <button>Delete Event</button>
        </div>
      )) }
    </div>
  );
}

export default App;
