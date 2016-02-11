function initialize() {
  var myLatlng = new google.maps.LatLng(-1.9446696,30.089721);
  var mapOptions = {
    zoom: 14,
    center: myLatlng
  }
  var map = new google.maps.Map(document.getElementById('klab-map'), mapOptions);
  var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: 'kLab',
      icon: kLabImageMapLogo
  });
}

google.maps.event.addDomListener(window, 'load', initialize);