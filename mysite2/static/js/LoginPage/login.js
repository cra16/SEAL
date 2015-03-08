$(document).ready(function(){
	$("#login").click(function(){
		var username = $("#username").val();
		var password = $("#password").val();
		//check if there is blank fields
		if(username == "" || password == ""){
			$('input[type="text"], input[type="password"]').css("border", "2px solid red");
			$('input[type="text"], input[type="password"]').css("box-shadow", "0 0 3px red");
			alert("Please fill in the fields.");
		}
		else{
			$.post("loginpractice.php", {username1: username, password1: password}, function(data){
				if(data == 0){
					$('input[type="text"], input[type="password"]').css({"border": "2px solid red", "box-shadow":"0 0 3px red"});
					alert('Username or Password is wrong!');
				}
				else if(data == 1){
					window.location.href = "../seal/html/index.html";
				}
				else{
					alert(data);
				}
			});
		}
	});

	$('#register').click(function(){
		window.location.href = "../mysite2/Confirm";
	});
});