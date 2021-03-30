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
	$('.comment_delete_btn').click(function() {
		var commentIdVar;
		commentIdVar = $(this).attr('data-commentid');
		
		$.get('/remove_comment/',
			{'comment_id': commentIdVar},
			function(data) {
				if ( data == 0) {
					$('#cid-' + commentIdVar).remove();
				}
			})
	});
});