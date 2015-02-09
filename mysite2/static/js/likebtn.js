$(function(){
	$('#likebutton').click(function(){
		confirm = window.confirm("Correct?");
		if(confirm){
			window.location.href = "../html/recommend.html";
		}
	});
});