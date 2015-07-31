$(document).ready(function() {

    $('.message .glyphicon').css('cursor','pointer');
    
    $('.message .glyphicon').on('click', function() {
      $(this).closest('.message').fadeOut();
    });

    $('#bell_notice').popup({
    title   : '알림',
    content : '읽지 않은 메시지가 1개 있습니다.',
    hoverable: true,
    delay: {
      show: 200,
      hide: 400
    }
    
  });
    
    $('.fullscreen.modal').modal('show');
$("div").on('click',"#cname",function(event){
        event.stopPropagation();
        $(this).unbind("click");
        CurrentPage=$(this).parent().parent().parent().parent().parent().attr("id");
        
        $.ajax(
            { url : "/mysite2/Select_Course/",
              data : {'Course' : $(this).text(),
                      'Page': "0",
                      'Current':CurrentPage
                    },
              sync : true,
              type : "POST",
              success:function(resp){  
                  
                  if(CurrentPage=="FirstPage")
                    $('#FirstPage').html(resp);
                  else if(CurrentPage=="SecondPage")
                    $('#SecondPage').html(resp);
                  else if(CurrentPage=="AllPage")
                    $('#AllPage').html(resp);
                  else if(CurrentPage=="SearchPage")
                    $('#SearchPage').html(resp);
    
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용                  
                } 

          });
         
    });
    
});


