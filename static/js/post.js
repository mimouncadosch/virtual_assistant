$(document).ready(function() {
	$('#msg').click(function(event) {
		var file_id = $(this).attr('file_id');
		var url = $(this).attr('url');
		var full_url = url + 'markread/' + file_id;
		data = {read : true}
		 $.ajax({
		    type : "POST",
		    url : full_url,
		    data: JSON.stringify(data),
		    contentType: 'application/json;charset=UTF-8',
		    success: function(result) {
		        console.log(result);
		    }
		});
	});
});