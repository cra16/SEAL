$(document).ready(function(){
	$("#loginForm").submit(function(){
		var username = $("#UserID").val();
		var password = $("#UserPassword").val();
		//check if there is blank fields
		if(username == "" || password == ""){
			$('input[type="text"], input[type="password"]').css("border", "2px solid red");
			$('input[type="text"], input[type="password"]').css("box-shadow", "0 0 3px red");
			alert("Please fill in the fields.");
			return false;
		}
		else{
			if (document.getElementById("UserID") == "admin_seal" )
				document.loginForm.action = "/";
			document.loginForm.submit();
		}
	});

	$('#register').click(function(){
		window.location.href = "./Confirm";
	});
});