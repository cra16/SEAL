$(function(){

	var name = "{{user.Profile.LastName}}",
	    year = 14,
	    major = "전산전자공학부",
	    num1 = 3,
	    num2 = 4;

	$('#name').text(name);
	$('#year').text(year);
	$('#major').text(major);
	$('#num1').text(num1);
	$('#num2').text(num2);

});