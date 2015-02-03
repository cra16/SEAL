$(function(){

	var coursename1 = "도술학개론",
        pname1 = {{user.profile.LastName}},
        rnum1 = 13,

        coursename2 = "도술학개론",
        pname2 = "홍길동 교수님",
        rnum2 = 13,

        coursename3 = "도술학개론",
        pname3 = "홍길동 교수님",
        rnum3 = 13;

    $('#coursename1').text(coursename1);
    $('#pname1').text(pname1);
    $('#rnum1').text(rnum1);

    $('#coursename2').text(coursename2);
    $('#pname2').text(pname2);
    $('#rnum2').text(rnum2);

    $('#coursename3').text(coursename3);
    $('#pname3').text(pname3);
    $('#rnum3').text(rnum3);

});