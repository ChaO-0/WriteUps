$(function(){

	var send = function (mode,data,callback){
		$.ajax({
		  type: 'POST',
		  url: './index.php?mode='+mode,
		  dataType: 'json',
		  data:JSON.stringify(data),
		  success: callback,
		});
	};

	clickDLLink = function(i){
		var win = window.open("index.php?mode=readfile&id="+i,"dllink");
	}

	$("#btn_login").on("click",function(){
		send("login",{"loginid":$("#loginid").val(),"pass":$("#pass").val() },function(json){
			$("#loginid").val("");
			$("#pass").val("");
			if(json.msg=="ok"){
				var h = ($("#files").children()).length>0?"":"<tr><td></td><td></td><td></td></tr>";
				if(json.files.length > 0){
					for(var i=0;i<json.files.length;++i){
						filelink = "";
						h += "<tr><td>" + json.files[i].name + "</td><td><button class='dllink' onclick='clickDLLink(\""+json.files[i].id+"\")'>DL</button></td></tr>";
					}
				}
				$("#files").append(h);
				$("#files").show();
				$("#login").remove();

			} else {
				alert("Login Fail");
			}
		});
	});

	//Loaded
	$("#login").show();
});