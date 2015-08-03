$(document).ready(function () {

/*  var ccode = document.getElementsByName('ccode')
  var cname = document.getElementsByName('cname')
  var cprof = document.getElementsByName('cprof')
  var likenum1 = 5; 
  var elikenum1 = document.getElementById('likenum1');


  for(var i=0; i<ccode.length; i++)
  {
    ccode[i].textContent = document.getElementsByName('ccode')[i].innerHTML;
    cname[i].textContent = document.getElementsByName('cname')[i].innerHTML;
    cprof[i].textContent = document.getElementsByName('cprof')[i].innerHTML;
  }*/
    
    $("#sch-result").find(".for-select-child").each(function(i, e){
         event.stopPropagation();
          $(this).unbind("click");
      $("#sch-result").on("click","#sch-select" + (i+1),function(){
        $.ajax(
          { url : "/mysite2/Sel_lecture/",
            data : {"ccode" : $("#ccode" + (i+1)).text(),
                    "cname" : $("#cname" + (i+1)).text(),
                    "cprof" : $("#cprof" + (i+1)).text(),
                    "cperiod" : $("#cperiod" + (i+1)).text()
                  },
            type : "POST",
            success:function(resp){
              $('#rt_table').html(resp);
            },
            error:function(xhr, option, error){
              alert(xhr.status);
              alert(error);
            }

          });
          $('#sch-result').fadeOut(100);
      });    
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
              sync : true,
              type : "POST",
              success:function(resp){  
                  $('#sch-result').html(resp);
                   
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용                  
                } 

          });
        $('#sch-result').fadeIn();
        $("div").off("click","#sch-search");  
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
              type : "POST",
              success:function(resp){         
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
              type : "POST",
              success:function(resp){  
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
              type : "POST",
              success:function(resp){                  
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
                    'Period': $('#Period').attr("name")
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
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
              async:true,
              success:function(resp){     
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
                    'Period': $('#Period').attr("name")
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
               $('#sch-result').html(resp);
                
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
          });
    });

    
});