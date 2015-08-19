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
    /*
    $('div').on('click','#FirstMajor',function(){
      event.stopPropagation();
      $(this).unbind("click");
        $.ajax(
            { url : "/mysite2/FirstPage/",
              data : {
                      'Page': "0"
                     },
              datatype : "json",
              type : "POST",

              success:function(resp){
                  
                  $('#FirstPage').html(resp);
                     
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });
      });
    $('div').on('click','#SecondMajor',function(){
      event.stopPropagation();
          $(this).unbind("click");
        $.ajax(
            { url : "/mysite2/SecondPage/",
              data : {
                           'Page': "0"
                    },
              type : "POST",
              success:function(resp){      

                  $('#SecondPage').html(resp);
                     
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });
      });

      $('div').on('click','#All',function(){
        event.stopPropagation();
          $(this).unbind("click");
        $.ajax(
            { url : "/mysite2/ThirdPage/",
              data : {'Page': "0"
                    },
              datatype : "json",
              type : "POST",
              success:function(resp){         
                  $('#ThirdPage').html(resp);
     
                     
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });
        });
*/



        $('div').on('click',"#Page",function(event){
          event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")
          
          if(CurrentPage=="SearchPageNation")
              Course = $('#CourseName').val();
          else
              Course = "";
        $.ajax(
            { url : "/mysite2/Page/",
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
                  else
                      $('#Search_Page').html(resp);
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
              Course = $('#CourseName').val();
          else
              Course = "";
        $.ajax(
            { url : "/mysite2/Page/",
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
                  else
                      $('#Search_Page').html(resp);
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
              Course = $('#CourseName').val();
          else
              Course = "";
        $.ajax(
            { url : "/mysite2/Page/",
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
                  else
                        $('#Search_Page').html(resp);
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
            { url : "/mysite2/SearchPage/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':$("#cname").text()
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
              success:function(resp){     
                       $('#Search_Page').html(resp);
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
            { url : "/mysite2/SearchPage/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':$("#cname").text()
                      
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
              success:function(resp){     
                  $('#Search_Page').html(resp);
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
            { url : "/mysite2/SearchPage/",
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage,
                      'Course':$("#cname").text()
                    },
              
              datatype:"json",
              type : "POST",
              async : false,
              success:function(resp){     
                  $('#Search_Page').html(resp);
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
            { url : "/mysite2/Page/",
              data : {'Page': "0",
                      'Current':"FirstPage",

                    },
              
              datatype:"json",
              type : "POST",
              async:false,
              success:function(resp){     
                       $('#FirstPage').html(resp);
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
            { url : "/mysite2/Page/",
              data : {'Page': "0",
                      'Current':"SecondPage",

                    },
              
              datatype:"json",
              type : "POST",
              async:false,
              success:function(resp){     
                       $('#SecondPage').html(resp);
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
            { url : "/mysite2/Page/",
              data : {'Page': "0",
                      'Current':"ThirdPage",

                    },
              
              datatype:"json",
              type : "POST",
              async:false,
              success:function(resp){     
                        $('#ThirdPage').html(resp);
                   },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });
});


