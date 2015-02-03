$(function(){

	var name = {{%user.profile.LastName%}},
	    year = {{%user.profile.StuNumber%}},
	    major ={{%user.profile.FirstMajor%}},
	    num1 = 3,
	    num2 = 4;

	$('#name').text(name);
	$('#year').text(year);
	$('#major').text(major);
	$('#num1').text(num1);
	$('#num2').text(num2);

});