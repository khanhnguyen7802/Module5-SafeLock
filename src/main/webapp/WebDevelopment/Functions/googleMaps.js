// Initialize and add the map
let map;

async function initMap() {
    // The location of Uluru
    // fetch location
    console.log("Generating map");
    let username = window.location.search;
    username = username.split("?")[1];
    let formData = new URLSearchParams();
    formData.append('username', username);
    fetch("http://localhost:8080/SAFEty/api/gps",
        {
            method: "POST",
            body: formData,
            headers: {
                "Content-type" : "application/x-www-form-urlencoded"
            }
        }
    ).then(
        response => {
            if (response.ok) {
                window.location.href = "../index.html";
            }
        }
    )
    const latitude = Math.random() * 170 - 85;
    console.log(latitude);
    const longitude = Math.random() * 360 - 180;
    console.log(longitude);
    const position = { lat: latitude, lng: longitude };

    // Request needed libraries.
    //@ts-ignore
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    // The map, centered at Uluru
    map = new Map(document.getElementById("map"), {
        zoom: 4,
        center: position,
        mapId: "DEMO_MAP_ID",
    });

    // The marker, positioned at Uluru
    const marker = new AdvancedMarkerElement({
        map: map,
        position: position,
        title: "Uluru",
    });
}
initMap();

async function resetMap() {
    document.getElementById("map").remove();
    initMap();
}

