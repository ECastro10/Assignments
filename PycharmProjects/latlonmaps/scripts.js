/**
 * Created by Lexi on 1/6/2017.
 */
var lat = 0;
var lng = 0;

$(function () {

    $('#submit').on('click', function () {
        var address = $('#address').val();
        $.ajax({
            type: 'GET',
            url: 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=AIzaSyAGvMFbhks3sEYX6ALK-K1B1wFgJfOMzQk',

            success: function (data) {

                lat = data.results[0].geometry.location.lat;
                lng = data.results[0].geometry.location.lng;
                var map = new google.maps.Map(document.getElementById('map'), {
                    zoom: 8,
                    center: {lat: lat, lng: lng}
                });
                var marker = new google.maps.Marker({
                map: map,
                position: data.results[0].geometry.location
                    });
                        $.ajax({
                        type: 'GET',
                        url: 'https://developer.trimet.org/ws/V1/stops/?ll=' + lng + ',' + lat + '&meters=300&appID=7AC167B85DD23A1D00D1B4DD1?&json=true',


                    success: function (data) {

                                var Array = data.resultSet.location;
                                for (var i=0; i<Array.length; i++) {
                                    // var stopLat = Array[i].lat;
                                    // var stopLng = Array[i].lng;
                                    var marker = new google.maps.Marker({
                                        map: map,
                                        position: Array[i]
                                    });

                                    // console.log(stopLat);
                                    // console.log(stopLng);
                                }

                            // console.log(data);

           }
        });
                }

        });



    });
});


// AIzaSyAGvMFbhks3sEYX6ALK-K1B1wFgJfOMzQk
//https://developer.trimet.org/ws/V1/stops/?ll=-122.65906999999999,45.52274509999999&meters=100&appID=7AC167B85DD23A1D00D1B4DD1?&json=true