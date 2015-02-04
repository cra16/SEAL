$(function(){

	var name = '{{ user.profile.LastName }}';
	var year = '{{ user.profile.StuNumber }}';
	var major ='{{ user.profile.FirstMajor }}';
	var num1 = 3;
	var num2 = 4;

	$('#name').text(name);
	$('#year').text(year);
	$('#major').text(major);
	$('#num1').text(num1);
	$('#num2').text(num2);

});