function toggleMapFunction() {
	if( $('#map-container').is(':hidden') ) {
		$("#map-container").css("display", "initial");
		$("#img-container").css("display", "none");
		$('#map-toggle').html("Show Picture");
	}
	else {
		$("#map-container").css("display", "none");
		$("#img-container").css("display", "initial");
		$('#map-toggle').html("Show Location");
	}
}

$(document).ready(function(){
	var img_width = $('#picture_image').width();
	var img_height = $('#picture_image').height();
	$('#map-container').width(img_width);
	$('#map-container').height(img_height);
	//$('#map-container').append("<div id='map'>");
	$('#map-container').append("<div id='map' style='width: " + img_width + "px; height: " + img_height + "px;'>");
	$("#map-container").css("display", "none");
	mapboxgl.accessToken = 'pk.eyJ1IjoiMjQ2OTgxMWIiLCJhIjoiY2ttdWtuZ2RjMHZ5MzJ3bXc3b3J4N29ieSJ9.rR1dAX-utT26r3bIQRbcjA';
	var map = new mapboxgl.Map({
	container: 'map', // container ID
	style: 'mapbox://styles/mapbox/streets-v11', // style URL
	center: [$('#like_btn').attr('data-longitude'), $('#like_btn').attr('data-latitude')], // starting position [lng, lat]
	zoom: 9 // starting zoom
	});
	var marker = new mapboxgl.Marker()
		.setLngLat([$('#like_btn').attr('data-longitude'), $('#like_btn').attr('data-latitude')])
			.addTo(map);
});