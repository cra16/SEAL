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
        CurrentPage=$(this).parent().parent().parent().parent().parent().parent().attr("id");
        var Parent=$(this).parent().parent().parent();
        var Code = Parent.find("[id=ccode]").text();
        var prof = Parent.find("[id=professor]").val();
        var period = Parent.find("[id=period]").val();
        var semester = Parent.find("[id=semester]").val();
        $.ajax(
            { url : "/mysite2/Select_Course/",
              data : {'Course' : $(this).text(),
                      'Page': "0",
                      'Current':CurrentPage,
                      'Code':Code,
                      'Professor':prof,
                      'Period':period,
                      'Semester':semester

                    },
              sync : true,
              type : "POST",
              success:function(resp){  
                  
                  if(CurrentPage=="FirstPage")
                    $('#FirstPage').html(resp);
                  else if(CurrentPage=="SecondPage")
                    $('#SecondPage').html(resp);
                  else if(CurrentPage=="ThirdPage")
                    $('#ThirdPage').html(resp);
                  else if(CurrentPage=="Search_Page")
                    $('#Search_Page').html(resp);
    
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용                  
                 } 

          });

         
    });
 

    $('div').on('click',"#CoursePage",function(event){
          event.stopPropagation();
          $(this).unbind("click");

          var CurrentPage=$(this).parent().parent().parent().attr("id");
       
        $.ajax(
            { url : "/mysite2/Page/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':$("#CourseHidden").val()
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
                  if(CurrentPage =="FirstPage")
                       $('#FirstPage').html(resp);
                  else if(CurrentPage =="SecondPage")
                        $('#SecondPage').html(resp);
                  else
                        $('#ThirdPage').html(resp);
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });

     



    });

    $('div').on('click','#CourseNext',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().parent().parent().attr("id");

        $.ajax(
            { url : "/mysite2/Page/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':$("#CourseHidden").val()
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
                  if(CurrentPage =="FirstPage")
                       $('#FirstPage').html(resp);
                  else if(CurrentPage =="SecondPage")
                        $('#SecondPage').html(resp);
                  else
                        $('#ThirdPage').html(resp);
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });

    $('.ui.sticky').sticky({
      context: '#sticky',
      pushing: true
    });

    $('div').on('click','#CoursePrevious',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().parent().parent().attr("id");

        $.ajax(
            { url : "/mysite2/Page/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':$("#CourseHidden").val()
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
                  if(CurrentPage =="FirstPage")
                       $('#FirstPage').html(resp);
                  else if(CurrentPage =="SecondPage")
                        $('#SecondPage').html(resp);
                  else
                        $('#ThirdPage').html(resp);
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });

         
});


