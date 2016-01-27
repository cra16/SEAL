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
        var Code = Parent.find("[name=ccode]").text();
        var prof = Parent.find("[id=professor]").val();
        var period = Parent.find("[id=period]").val();
        var semester = Parent.find("[id=semester]").val();
        $.ajax(
            { url : "/Select_Professor/",
              data : {
                      'Course' : $(this).text(),
                      'Page': "1",
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
 
  $("div").on('click',"#professorSl",function(event){
        event.stopPropagation();
        $(this).unbind("click");
        CurrentPage=$(this).parent().parent().parent().parent().attr("id");

        var Parent=$(this).parent();
        var Course = Parent.find("[id=cname]").text();
        var Code = Parent.find("[name=ccode]").text();
        var prof = Parent.find("[id=professor]").val();
        var period = Parent.find("[id=period]").val();
        var semester = Parent.find("[id=semester]").val();
        $.ajax(
            { url : "/Select_Course/",
              data : {
                      'Course' : Course,
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
    $('div').on('click',"#CoursePageData",function(event){
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

  
    $('div').on('click','#CoursePrevious',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().parent().parent().attr("id");
          var CurrentCourse = $(this).parent().find("[id=CourseHidden]").val();
        $.ajax(
            { url : "/Select_Professor/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':CurrentCourse,
     
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
  

    $('div').on('click',"#ProPage",function(event){
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

    $('div').on('click','#ProNext',function(){
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
    
    $('div').on('click',"#BackButton",function(event){
          event.stopPropagation();
          $(this).unbind("click");

          var CurrentPage=$(this).parent().attr("id");
          var CurrentCourse = $(this).parent().find("[id=CourseHidden]").val();
        $.ajax(
            { url : "/Page/",
              data : {'Page': "0",
                      'Current':CurrentPage,
                      
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



    $(document).keydown(function(e){

     
    });

  $('.ui.sticky').sticky({
      context: '#sticky',
      pushing: true
    });

});


$(function(){


$.fn.starvalue = function() {
    return $(this).each(function() {
        // Get the value
        var val = parseFloat($(this).html());
        // Make sure that the value is in 0 - 5 range, multiply to get width
        var size = Math.max(0, (Math.min(5, val))) * 16;
        // Create stars holder
        var $span = $('<span />').width(size);
        // Replace the numerical value with stars
        $(this).html($span);
    });
}

$('span.starvalue').starvalue();


});


