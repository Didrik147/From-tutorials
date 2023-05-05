mapboxgl.accessToken = 'pk.eyJ1IjoiZGlkcmlrMTQ3IiwiYSI6ImNreTdsODVvMjE3MG8ycXFuYXF5cDFjeWUifQ.J_49_XRBUjecT7OVrF4hAQ';

navigator.geolocation.getCurrentPosition(successLocation, errorLocation, {
    enableHighAccuracy: true
});

function successLocation(position){
    //console.log(position)
    
    //Bogerud T
    let latlon = [59.876077430581894, 10.842078483720146]
    let lonlat = [latlon[1], latlon[0]]

    setupMap(lonlat)
    //setupMap([position.coords.longitude, position.coords.latitude])
}

function errorLocation(){
    // Oslo
    setupMap([10.7522, 59.9139])
}

function setupMap(center){
    const map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v9',
        center: center,
        zoom: 15
    });

    const nav = new mapboxgl.NavigationControl();
    map.addControl(nav);    

    var directions = new MapboxDirections({
        accessToken: mapboxgl.accessToken,
        unit: 'metric',
        profile: 'mapbox/cycling'
      });
      
      map.addControl(directions, 'top-left');

}


