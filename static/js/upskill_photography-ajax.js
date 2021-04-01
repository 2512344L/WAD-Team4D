$(document).ready(function() {
	try {
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
	} catch(err) {}
	try {
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
	} catch(err) {}
	try {
		$('.picture_delete_btn').click(function() {
			var pictureIdVar;
			pictureIdVar = $(this).attr('data-pictureid');
			
			$.get('/remove_picture/',
				{'picture_id': pictureIdVar},
				function(data) {
					if ( data == 0) {
						$('#pid-' + pictureIdVar).remove();
					}
				})
		});
	} catch(err) {}
});