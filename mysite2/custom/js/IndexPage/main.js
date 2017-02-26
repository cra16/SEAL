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
  



        $('div').on('click',"#Page",function(event){
          event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")
       
          if(CurrentPage=="SearchPageNation")
              Course = $('#CourseHidden').val();
          else
              Course = "";
        $.ajax(
            { url : "/Page/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':Course 
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
              success:function(resp){     
                  if(CurrentPage =="FirstPageNation")
                       $('#FirstPage').html(resp);
                  else if(CurrentPage =="SecondPageNation")
                        $('#SecondPage').html(resp);
                  else if(CurrentPage =="ThirdPageNation")
                        $('#ThirdPage').html(resp);
                  else if(CurrentPage =="SugangPageNation")
                        $('#SugangPage').html(resp);
                  else if(CurrentPage=="LikeSugangPageNation")
                        $("#LikeSugangPage").html(resp);
                  else
                      $('#Search_Page').html(resp);
                  $('[data-toggle="tooltip"]').tooltip(); 
                   $('span.starvalue').starvalue();

                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          
          });

     


    });

    $('div').on('click','#Next',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")
          
          if(CurrentPage=="SearchPageNation")
              Course = $('#CourseHidden').val();
          else
              Course = "";
        $.ajax(
            { url : "/Page/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':Course
                      
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
              success:function(resp){     
                  if(CurrentPage =="FirstPageNation")
                       $('#FirstPage').html(resp);
                  else if(CurrentPage =="SecondPageNation")
                        $('#SecondPage').html(resp);
                  else if(CurrentPage =="ThirdPageNation")
                        $('#ThirdPage').html(resp);
                  else if(CurrentPage=="SugangPageNation")
                        $('#SugangPage').html(resp);
                  else if(CurrentPage=="LikeSugangPageNation")
                        $("#LikeSugangPage").html(resp);
                  else
                      $('#Search_Page').html(resp);
                  $('[data-toggle="tooltip"]').tooltip(); 
                   $('span.starvalue').starvalue();

                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });

    $('div').on('click','#Previous',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")
   
          if(CurrentPage=="SearchPageNation")
              Course = $('#CourseHidden').val();
          else
              Course = "";
        $.ajax(
            { url : "/Page/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':Course
                    },
              
              datatype:"json",
                type : "POST",
              async:true,
              success:function(resp){     
                  if(CurrentPage =="FirstPageNation")
                       $('#FirstPage').html(resp);
                  else if(CurrentPage =="SecondPageNation")
                        $('#SecondPage').html(resp);
                  else if(CurrentPage =="ThirdPageNation")
                        $('#ThirdPage').html(resp);
                  else if(CurrentPage=="SugangPageNation")
                        $('#SugangPage').html(resp);
                  else if(CurrentPage=="LikeSugangPageNation")
                        $("#LikeSugangPage").html(resp);
                  else
                        $('#Search_Page').html(resp);
                  $('[data-toggle="tooltip"]').tooltip(); 
                   $('span.starvalue').starvalue();

                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });

         $('div').on('click',"#SearchPage",function(event){
          event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

        $.ajax(
            { url : "/SearchPage/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':$("#cname").text()
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
              success:function(resp){     
                       $('#Search_Page').html(resp);
                       $('[data-toggle="tooltip"]').tooltip(); 

                 },
                error: function(xhr, option, error){
                  alert(xhr.status); //ì˜¤ë¥˜ì½”ë“œ
                  alert(error); //ì˜¤ë¥˜ë‚´ìš©

                  } 
            
          
          });

     



    });

    $('div').on('click','#SearchNext',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

        $.ajax(
            { url : "/SearchPage/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':$("#cname").text()
                      
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
              success:function(resp){     
                  $('#Search_Page').html(resp);
                  $('[data-toggle="tooltip"]').tooltip(); 
                   $('span.starvalue').starvalue();

                },
                error: function(xhr, option, error){
                  alert(xhr.status); //ì˜¤ë¥˜ì½”ë“œ
                  alert(error); //ì˜¤ë¥˜ë‚´ìš©

                  } 
            
          });



    });

    $('div').on('click','#SearchPrevious',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

        $.ajax(
            { url : "/SearchPage/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':$("#cname").text()
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
              success:function(resp){     
                  $('#Search_Page').html(resp);
                  $('[data-toggle="tooltip"]').tooltip(); 
                   $('span.starvalue').starvalue();

                },
                error: function(xhr, option, error){
                  alert(xhr.status); //ì˜¤ë¥˜ì½”ë“œ
                  alert(error); //ì˜¤ë¥˜ë‚´ìš©

                  } 
            
          });


    });

    $('div').on('click','#FirstMajor',function(){
       event.stopPropagation();
          
        $.ajax(
            { url : "/Page/",
              data : {'Page': "0",
                      'Current':"FirstPage",

                    },
              
              datatype:"json",
              type : "POST",
              async:false,
              success:function(resp){     
                       $('#FirstPage').html(resp);
                       $('[data-toggle="tooltip"]').tooltip(); 
                        $('span.starvalue').starvalue();

                 },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });

     $('div').on('click','#SecondMajor',function(){
       event.stopPropagation();
       
        $.ajax(
            { url : "/Page/",
              data : {'Page': "0",
                      'Current':"SecondPage",

                    },
              
              datatype:"json",
              type : "POST",
              async:false,
              success:function(resp){     
                       $('#SecondPage').html(resp);
                       $('[data-toggle="tooltip"]').tooltip();
                        $('span.starvalue').starvalue(); 

                 },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });
     $('div').on('click','#All',function(){
       event.stopPropagation();
        
        $.ajax(
            { url : "/Page/",
              data : {'Page': "0",
                      'Current':"ThirdPage",

                    },
              
              datatype:"json",
              type : "POST",
              async:false,
              success:function(resp){     
                        $('#ThirdPage').html(resp);
                        $('span.starvalue').starvalue();
                        $('[data-toggle="tooltip"]').tooltip(); 

                   },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });
     $('div').on('click','#SugangMajor',function(){
       event.stopPropagation();
        
        $.ajax(
            { url : "/Page/",
              data : {'Page': "0",
                      'Current':"SugangPage",

                    },
              
              datatype:"json",
              type : "POST",
              async:false,
              success:function(resp){     
                        $('#SugangPage').html(resp);
                        $('[data-toggle="tooltip"]').tooltip(); 
                         $('span.starvalue').starvalue();

                   },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });




    });

     $('div').on('click','#LikeMajor',function(){
       event.stopPropagation();
        
        $.ajax(
            { url : "/Page/",
              data : {'Page': "0",
                      'Current':"LikeSugangPage",

                    },
              
              datatype:"json",
              type : "POST",
              async:false,
              success:function(resp){     
                        $('#LikeSugangPage').html(resp);
                        $('[data-toggle="tooltip"]').tooltip(); 
                         $('span.starvalue').starvalue();

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

        $(this).hide();
        $(Find).show();
    });
    $('div').on('click',"#Open",function(event){
       event.stopPropagation();
        $(this).unbind("click");
        var Find = $(this).parent().find("[id=Close]");

        $(this).hide();
        $(Find).show();
    });    
    $('body').on('click','.course_edit',function(event){
        event.stopPropagation();
          $(this).unbind("click");
            var Parent = $(this).closest(".sugang-box")
            var Code = Parent.find("[name=ccode]").text();
            var CourseName=Parent.find("[name=cname]").text();
            var prof = Parent.find("[name=cprof]").attr("value");
            var period = Parent.find("[name=period]").attr("value");
            var semester = Parent.find("[name=csem]").attr("value");
            var CourseID = $(this).parent().attr("id");

            var form =document.createElement("form");
            form.method ="POST";
            form.action = "/UpdateCourse/"
            var inputdata ={
              'Code':Code,
                      'CourseName': CourseName,
                      'Professor':prof,
                      'Semester':semester,
                      'CourseID':CourseID,
            }
            var input; 
            for(key in inputdata)
            {
              input= document.createElement("input");
              input.name =key;
              input.value=inputdata[key];
              input.type="hidden";
              form.appendChild(input);
            }
            $("body").append(form);
            form.submit();    
             
          



    });

});


