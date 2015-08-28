$(document).ready(function() {

$('div').on('click','#likebutton',function(event){ 
	event.stopPropagation();
	$(this).unbind("click");
    confirm1 = window.confirm("이 강의를 추천하시겠습니까?");
            if(confirm1){
                window.location.href = "/Recommend/" + $(this).attr('name');
            }
    });

});