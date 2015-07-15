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
    
    
    $('.table td').css( 'cursor', 'pointer' );
    
    var arr=['월', '화', '수', '목', '금', '토'];
    
    $("div").on("click",'.table td',function(event) {
      event.stopPropagation();
      if(confirm((arr[$(this).index()-1]) + "요일 " + ($(this).parent().index()+1) + "교시 수업을 검색하시겠습니까?")==true){
          // $('#sch-result').fadeIn();
          location.href = '/mysite2/sel_period/' + (arr[$(this).index()-1]) + ($(this).parent().index()+1) + '/' + 1
        };
    });

    $("div").on("click","#sch-select",function(event){
      event.stopPropagation();
      var parent=$(this).parent().parent().parent();
      var Code = parent.find("[id=ccode]").text();
      var name = parent.find("[id=cname]").text();
      var prof = parent.find("[id=cprof]").text();
      var period = $(this).parent().find("[id=cperiod]").text();
      alert(Code);
      alert(period);
      $.ajax(
        { url : "/mysite2/Sel_lecture/",
          data : {"ccode" : Code,
                  "cname" : name,
                  "cprof" : prof,
                  "cperiod" : period
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
        
    });
    /*
    $('#sch-search').click(function(event) {
       
    });
    */
    $('#sch-result .button').click(function(event) {
        $('#sch-result').fadeOut(100);
    });
		
    $("div").on("click",'#sch-search',function(){
        
        $.ajax(
            { url : "/mysite2/Schedule/",
              data : {'major' : $('#major').val(),
                      'category': $('#category').val(),
                      'SearchName': $('#SearchName').val(),
                      'Page': "0"
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

    $('*').keypress(function(e){

      if(e.keyCode==13)
        return false;
    });

    $('div').on('click','#Previous',function(){
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

    $('div').on('click','#Next',function(){

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

    $('div').on('click','#Page',function(){ 

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
                    'Period':period
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

    var url = location.href;
    var Firstindex = url.indexOf('/',3);
    var Lastindex = url.indexOf('/',4);
    
    var period = url.substring(Firstindex,Lastindex);

    $('div').on('click','#LecPage',function(event){ 

           event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

         $.ajax(
            { url : "/mysite2/Sel_periodLecture/",
              data : {'Page': $(this).attr("name"),
                    'Period':period
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
                    'Period':period
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

    $("td").on('click',"#del_my_lec",function(event){
         event.stopPropagation();

       var Data=$(this).parent().text();
        

        var Firstindex =Data.indexOf('.')
        
        var Secondindex =Data.indexOf('.',Firstindex+1)
        
        var CodeFirst = Data.substring(0,Data.indexOf('.'));
        
        var Code = CodeFirst.substring(CodeFirst.lastIndexOf(' ')+1);
        var Course = Data.substring(Firstindex+1,Data.indexOf('(',Firstindex+1));
        var profFirst = Data.substring(Secondindex+1);
        var prof = profFirst.substring(0, profFirst.indexOf("  ")-1);
        
          $.ajax(
            { url : "/mysite2/Sel_periodDelete/",
              data : {"ccode" : Code,
                      "cname" : Course,
                      "cprof" : prof,
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
               $('#rt_table').html(resp);
                alert("삭제가 완료되었습니다.")
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });
    });

});