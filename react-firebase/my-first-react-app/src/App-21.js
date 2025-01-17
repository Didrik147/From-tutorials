import './App.css';
// hooks start with use
import { useState } from 'react'

function App() {
  // Each object is a single event
  const [events, setEvents] = useState([
    { title: "Mario's birthday bash", id: 1 },
    { title: "Bowser's live stream", id: 2 },
    { title: "Race on Moo Moo Farm", id: 3 }
  ])

  const handleClick = (id) => {
    setEvents((prevEvents) => {
      return prevEvents.filter((event) => {
        return id !== event.id
      })
    })
    console.log(id)
  }


  return (
    <div className="App">
      {events.map((event, index) => (
        <div key={event.id}>
          <h2>{index} - {event.title}</h2>
          <button onClick={() => handleClick(event.id)}>Delete Event</button>
        </div>
      ))}
    </div>
  );
}

export default App;
