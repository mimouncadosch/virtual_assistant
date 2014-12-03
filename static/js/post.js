function postFile(file, filename) {
	var http = new XMLHttpRequest();
	var url = "http://104.236.4.64/upload";
	//var params = "lorem=ipsum&name=binny";
	http.open("POST", url, true);

	//Send the proper header information along with the request
	http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	//http.setRequestHeader("Content-length", params.length);
	http.setRequestHeader("Connection", "close");

	http.onreadystatechange = function() {//Call a function when the state changes.
		if(http.readyState == 4 && http.status == 200) {
			alert(http.responseText);
		}
	}
	
	var formData = new FormData();
	console.log("posting ", file, "as " , filename);
	formData.append(filename, file);
	http.send(formData);
	//http.send(params);
}

function postTest() {
	postFile("test.txt", "uploaded.txt");
}
