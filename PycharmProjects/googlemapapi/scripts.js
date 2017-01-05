/**
 * Created by Lexi on 1/3/2017.
 */
//AIzaSyCNDQ7OsF5aei-6FHX3WfFbwXzBtMSHN54


var map;
var element = document.getElementById('map');

function initMap() {
    map = new google.maps.Map(element, {
        center: {lat: lat, lng: lon},
        zoom:8
    });
}


$('#submit').click(function() {
   var lat = $('#lat').val();
   lat = parseFloat(lat);
   var lon = $('#lon').val();
   lon = parseFloat(lon);
   console.log(lat);
   console.log(lon);
  map = new google.maps.Map(element, {
        center: {lat: lat, lng: lon},
        zoom:8
    });

});


