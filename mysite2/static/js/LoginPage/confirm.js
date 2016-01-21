$(document).ready(function(){
	$("#confirmForm").submit(function(){
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
			$('#registerCon').fadeIn();
			$('#preloader').fadeIn();
        	$('#status').fadeIn(); // will first fade out the loading animation
        	setTimeout(function()
     		{
     			alert('서버가 느리네요...');
     		},30000)
}

        	$('#preloader').delay(30000).fadeOut('slow'); // will fade out the white DIV that covers the website3
        	$('body').delay(300).css({'overflow':'visible'});

     		
});
	$('#cancel').click(function(){
		window.location.href = "../";
	});
});