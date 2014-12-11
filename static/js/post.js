$(document).ready(function() {
	$('#post_msg').click(function(event) {
		var file_id = generateID();
		var url = $('textarea').attr('url');
		// var full_url = url + '/' + file_id;
		var text = $('textarea#msg').val();
		var data =  {	text : text, 
						file_id : file_id
					}
		 $.ajax({
		    type : "POST",
		    url : url,
		    data: JSON.stringify(data),
		    contentType: 'application/json;charset=UTF-8',
		    success: function(result) {
		        console.log(result);
		    }
		});
	});
});

// generate id as hash of date and random value
function generateID() {
  var current_date = (new Date()).valueOf().toString();
  var random = Math.random().toString();
  var id = Sha1.hash(current_date + random);
  return id;
}
