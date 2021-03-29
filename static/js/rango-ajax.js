$(document).ready(function() {
	$('#like_btn').click(function() {
		var pictureIdVar;
		pictureIdVar = $(this).attr('data-pictureid');
		
		$.get('/like_picture/',
			{'picture_id': pictureIdVar},
			function(data) {
				$('#like_count').html(data);
				$('#like_btn').hide();
			})
	});
});