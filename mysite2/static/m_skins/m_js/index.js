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
            { url : "/Select_Course/",
              data : {'Course' : $(this).text(),
                      'Page': "0",
                      'Current':CurrentPage,
                      'Code':Code,
                      'Professor':prof,
                      'Period':period,
                      'Semester':semester

                    },
              async : false,
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
 
  $("div").on('click',"#professorSl",function(event){
        event.stopPropagation();
        $(this).unbind("click");
        CurrentPage=$(this).parent().parent().parent().parent().attr("id");

        var Parent=$(this).parent();
        var Course = Parent.find("[id=cname]").text();
        var Code = Parent.find("[id=ccode]").text();
        var prof = Parent.find("[id=professor]").val();
        var period = Parent.find("[id=period]").val();
        var semester = Parent.find("[id=semester]").val();
        $.ajax(
            { url : "/Select_Professor/",
              data : {'Course' : Course,
                      'Page': "0",
                      'Current':CurrentPage,
                      'Code':Code,
                      'Professor':prof,
                      'Period':period,
                      'Semester':semester,
                      'ProSelect':"1"

                    },
              async : false,
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
          var CurrentCourse = $(this).parent().find("[id=CourseHidden]").val();
        $.ajax(
            { url : "/Page/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':CurrentCourse
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
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
          var CurrentCourse = $(this).parent().find("[id=CourseHidden]").val();
        $.ajax(
            { url : "/Page/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':CurrentCourse
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
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

  
    $('div').on('click','#ProPrevious',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().parent().parent().attr("id");
          var CurrentCourse = $(this).parent().find("[id=CourseHidden]").val();
        $.ajax(
            { url : "/Select_Professor/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':CurrentCourse,
                      'ProSelect':1
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
              success:function(resp){     
                  if(CurrentPage =="FirstPageNation" || CurrentPage == "FirstPage")
                       $('#FirstPage').html(resp);
                  else if(CurrentPage =="SecondPageNation"|| CurrentPage == "SecondPage")
                        $('#SecondPage').html(resp);
                  else if(CurrentPage =="ThirdPageNation" || CurrentPage == "ThirdPage")
                        $('#ThirdPage').html(resp);
                  else
                    $("#Search_Page").html(resp);
                },
                error: function(xhr, option, error){

                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });
  

    $('div').on('click',"#ProNext",function(){
          event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().parent().parent().attr("id");
          alert(CurrentPage);
          var CurrentCourse = $(this).parent().find("[id=CourseHidden]").val();
        $.ajax(
            { url : "/Select_Professor/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':CurrentCourse,
                      'ProSelect':1
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
              success:function(resp){     
                  if(CurrentPage =="FirstPageNation" || CurrentPage == "FirstPage")
                       $('#FirstPage').html(resp);
                  else if(CurrentPage =="SecondPageNation"|| CurrentPage == "SecondPage")
                        $('#SecondPage').html(resp);
                  else if(CurrentPage =="ThirdPageNation" || CurrentPage == "ThirdPage")
                        $('#ThirdPage').html(resp);
                  else
                    $("#Search_Page").html(resp);
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });

     



    });

    $('div').on('click','#ProPrevious',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().parent().parent().attr("id");
          alert(CurrentPage);
          var CurrentCourse = $(this).parent().find("[id=CourseHidden]").val();
        $.ajax(
            { url : "/Select_Professor/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':CurrentCourse,
                      'ProSelect':1
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
              success:function(resp){     
                   if(CurrentPage =="FirstPageNation" || CurrentPage == "FirstPage")
                       $('#FirstPage').html(resp);
                  else if(CurrentPage =="SecondPageNation"|| CurrentPage == "SecondPage")
                        $('#SecondPage').html(resp);
                  else if(CurrentPage =="ThirdPageNation" || CurrentPage == "ThirdPage")
                        $('#ThirdPage').html(resp);
                  else
                    $("#Search_Page").html(resp);
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });

  
    $('div').on('click','#ProPrevious',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id");
          var CurrentCourse = $(this).parent().find("[id=CourseHidden]").val();
        $.ajax(
            { url : "/Select_Professor/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':CurrentCourse,
                      'ProSelect':1
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
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

$('div').on('click',"#Close",function(event){
         event.stopPropagation();
          $(this).unbind("click");
        var Find = $(this).parent().find("[id=Open]");
        alert("줄이기");
        $(this).hide();
        $(Find).show();
    });
    $('div').on('click',"#Open",function(event){
       event.stopPropagation();
          $(this).unbind("click");
        var Find = $(this).parent().find("[id=Close]");
        
        alert("더보기");
        $(this).hide();
        $(Find).show();
    });    

    $(document).keydown(function(e){

     
    });

  $('.ui.sticky').sticky({
      context: '#sticky',
      pushing: true
    });

});




