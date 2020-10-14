function generatePass() {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			var data = JSON.parse(this.responseText);
			var rpas = (data['random']);
			document.getElementById('password').value = rpas;
		}
	};
	xhttp.open("POST", "/users/register/generate", true);
	xhttp.send();
}

if (document.location.pathname == '/users/register'){
	generatePass();
}
