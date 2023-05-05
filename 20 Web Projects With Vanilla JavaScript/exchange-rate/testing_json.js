

function testJSON(){
    /* fetch('items.json', {
        method: 'POST',
        headers: {
            'Content-Type: application/json'
        }
    }) */

    fetch('items.json')
        .then(res => res.json())
        .then(data => document.body.innerHTML = data[0].text);
}

//testJSON();