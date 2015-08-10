$(document).ready(function () {

      $("#sch-result").on("click","#sch-select",function(){
          event.stopPropagation();
          $(this).unbind("click");
          var parent=$(this).parent().parent().parent();
          var Code = parent.find("[id=ccode]").text();
          var name = parent.find("[id=cname]").text();
          var prof = parent.find("[id=cprof]").text();
          var period = $(this).parent().find("[id=cperiod]").text();
             
        $.ajax(
          { url : "/mysite2/Sel_lecture/",
            data : {"ccode" : Code,
                    "cname" : name,
                    "cprof" : prof,
                    "cperiod" : period
                  },
            type : "POST",
            async : false,
            success:function(resp){
              $('#rt_table').html(resp);
            },
            error:function(xhr, option, error){
              alert(xhr.status);
              alert(error);
            }
          });
        $("#sch-result").fadeOut(100);
      });
    
    $("div").on("click",'#sch-search',function(event){
        event.stopPropagation();
        $(this).unbind("click");
 
        $.ajax(
            { url : "/mysite2/Schedule/",
              data : {'major' : $('#major').val(),
                      'category': $('#category').val(),
                      'SearchName': $('#SearchName').val(),
                      'Page': "0"
                    },
              async : false,
              type : "POST",
              success:function(resp){  
                $("#sch-result").off("click","#sch-select");
                $("div").off("click","#sch-search");
                  $('#sch-result').html(resp);
                   
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용                  
                } 

          });
        $('#sch-result').fadeIn();
        

    });

    $('*').keypress(function(e){

      if(e.keyCode==13)
        return false;
    });

    $('div').on('click','#Previous',function(event){
       event.stopPropagation();
       $(this).unbind("click");
        $.ajax(
            { url : "/mysite2/Schedule/",
              data : {'major' : $('#major').val(),
                      'category': $('#category').val(),
                      'SearchName': $('#SearchName').val(),
                      'Page': $('#Previous').attr('name')
                    },
              async : false,

              type : "POST",
              success:function(resp){       
                $("#sch-result").off("click","#sch-select");
                  $("div").off("click","#sch-search");
                  $('#sch-result').html(resp);
                     
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
          });
    
    });

    $('div').on('click','#Next',function(event){
         event.stopPropagation();
        $(this).unbind("click");
        $.ajax(
            { url : "/mysite2/Schedule/",
              data : {'major' : $('#major').val(),
                      'category': $('#category').val(),
                      'SearchName': $('#SearchName').val(),
                      'Page': $('#Next').attr('name')
                    },
              async : false,

              type : "POST",
              success:function(resp){  
                $("#sch-result").off("click","#sch-select");
                  $("div").off("click","#sch-search");
                  $('#sch-result').html(resp);
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
          });
   
    
    });

    $('div').on('click','#Page',function(event){ 
         event.stopPropagation();
         $(this).unbind("click");
        $.ajax(
            { url : "/mysite2/Schedule/",
              data : {'major' : $('#major').val(),
                      'category': $('#category').val(),
                      'SearchName': $('#SearchName').val(),
                      'Page': $(this).attr('name')
                    },
              async : false,

              type : "POST",
              success:function(resp){               
              $("#sch-result").off("click","#sch-select");  
                 $("div").off("click","#sch-search");   
                  $('#sch-result').html(resp);
               
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
          });
 
    });



        $('div').on('click','#LecPrevious',function(event){ 

         event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

         $.ajax(
            { url : "/mysite2/Sel_periodLecture/",
              data : {'Page': $(this).attr("name"),
                    'Period': $('#Period').attr("name"),
                    'SelectMajor': $('#SelectMajor').attr("name"),
                    'SelectCategory': $('#SelectCategory').attr("name"),
                    'SearchName': $('#SearchName').val() + ""

                    
                    },
              
              datatype:"json",
              type : "POST",
              async:false,
              success:function(resp){     
                $("#sch-result").off("click","#sch-select");
                $("div").off("click","#sch-search");   
               $('#sch-result').html(resp);
                
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
          });
    });

    
    
    $('div').on('click','#LecPage',function(event){ 

           event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

         $.ajax(
            { url : "/mysite2/Sel_periodLecture/",
              data : {'Page': $(this).attr("name"),
                    'Period': $('#Period').attr("name"),
                    'SelectMajor': $('#SelectMajor').attr("name"),
                    'SelectCategory': $('#SelectCategory').attr("name"),
                    'SearchName': $('#SearchName').val() + ""
                    },
              
              datatype:"json",
              type : "POST",
              async:false,
              success:function(resp){     
                 $("#sch-result").off("click","#sch-select");
                  $("div").off("click","#sch-search");   
               $('#sch-result').html(resp);
                
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
          });
        
    });

    $('div').on('click','#LecNext',function(event){ 

           event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

         $.ajax(
            { url : "/mysite2/Sel_periodLecture/",
              data : {'Page': $(this).attr("name"),
                    'Period': $('#Period').attr("name"),
                    'SelectMajor': $('#SelectMajor').attr("name"),
                    'SelectCategory': $('#SelectCategory').attr("name"),
                    'SearchName': $('#SearchName').val() + ""

                    },
              
              datatype:"json",
              type : "POST",
              async:false,
              success:function(resp){     
                $("#sch-result").off("click","#sch-select");
                $("div").off("click","#sch-search");
               $('#sch-result').html(resp);
                
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
          });
        
    });


    
});