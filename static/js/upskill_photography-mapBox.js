var aspect_ratio;
var map;
var picture_location_marker;

function toggleMapFunction() {
	if( $('#map-container').is(':hidden') ) {
		picture_location_marker = new mapboxgl.Marker()
			.setLngLat([$('#like_btn').attr('data-longitude'), $('#like_btn').attr('data-latitude')])
			.addTo(map);
		$('#map-container').width($('#center-column').width());
		$('#map-container').height($('#center-column').width() * aspect_ratio);
		$("#map-container").css("display", "initial");
		$("#img-container").css("display", "none");
		$('#map-toggle').html("Show Picture");
		map.zoom = 0;
	} else {
		picture_location_marker.remove();
		$("#map-container").css("display", "none");
		$("#img-container").css("display", "initial");
		$('#map-toggle').html("Show Location");
	}
}

$(document).ready(function(){
	aspect_ratio = $('#picture_image').height() / $('#picture_image').width();
	$( window ).resize(function() {
		if( $('#img-container').is(':hidden') ) {
			$("#map-container").css("display", "none");
			$("#img-container").css("display", "initial");
			$('#map-toggle').html("Show Location");
		}
		$('#map-container').width($('#center-column').width());
		$('#map-container').height($('#center-column').width() * aspect_ratio);
		$('#comment_column').height($('#center-column').width() * aspect_ratio);
	});
	$('#comment_column').height($('#center-column').width() * aspect_ratio);
	$('#map-container').append("<div id='map' style='width: " + $('#center-column').width() + "px; height: " + $('#center-column').width() * aspect_ratio + "px;'>");
	$("#map-container").css("display", "none");
	
	mapboxgl.accessToken = 'pk.eyJ1IjoiMjQ2OTgxMWIiLCJhIjoiY2ttdWtuZ2RjMHZ5MzJ3bXc3b3J4N29ieSJ9.rR1dAX-utT26r3bIQRbcjA';
	map = new mapboxgl.Map({
	container: 'map', // container ID
	style: 'mapbox://styles/mapbox/streets-v11', // style URL
	center: [$('#like_btn').attr('data-longitude'), $('#like_btn').attr('data-latitude')], // starting position [lng, lat]
	zoom: 9 // starting zoom
	});
	
});