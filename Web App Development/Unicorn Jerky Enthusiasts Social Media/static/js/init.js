
function getPostID(postdiv) {
	return postdiv.id.substring(postdiv.id.lastIndexOf('_')+1);
}

function sendPost() {
	var form = $('#post-form')[0];
	var data = new FormData(form);

	$('#sparkle').prop('disabled', 'true');
	
	$.ajax({
		type: 'POST',
		enctype: 'multipart/form-data',
		url: '/api/posts/',
		data: data,
		//processData: false,
		//contentType: false,
		success: insertPost,
		error: function() {
			alert('Unable to post. Please sparkle harder.');
			$('#sparkle').prop('disabled', false);
		}
	});

}
