$(document).ready(function(){
	$("#check").click(function(){
		var username = $("#username").val(),
		 	password = $("#password").val(),
		 	year = $("#year").val();
		//check if there is blank fields
		if(username == "" || password == "" || year == ""){
			$('input[type="text"], input[type="password"]').css("border", "2px solid red");
			$('input[type="text"], input[type="password"]').css("box-shadow", "0 0 3px red");
			alert("Please fill in the fields.");
		}
		else{
			$.post("confirm.php", {username1: username, password1: password, year1: year}, function(data){
				if(data == 0){
					$('input[type="text"], input[type="password"]').css({"border": "2px solid red", "box-shadow":"0 0 3px red"});
					alert('Username or Password is wrong!');
				}
				else if(data == 1){
					window.location.href = "register.html";
				}
				else{
					alert(data);
				}
			});
		}
	});

	$('#cancel').click(function(){
		window.location.href = "loginpractice.html";
	});
});