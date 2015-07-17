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
    
    $('.table td').click(function(event) {
      if(confirm((arr[$(this).index()-1]) + "요일 " + ($(this).parent().index()+1) + "교시 수업을 검색하시겠습니까?")==true){
          // $('#sch-result').fadeIn();
          location.href = '/mysite2/sel_period/' + (arr[$(this).index()-1]) + ($(this).parent().index()+1) + '/' + 1
        };
    });

    $("#sch-result").find(".for-select-child").each(function(i, e){
      $("#sch-select" + (i+1)).click(function(){
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
          
      });    
    });
    
    $("#table").find("td").each(function(i, e){
      $("#del-my-lec" + parseInt(i / 6) + "-" + (i % 6 + 1)).click(function(){
        $.ajax(
          { url : "/mysite2/Remove_lecture/",
            data : {"ccode" : $("#table-ccode" + parseInt(i / 6) + "-" + (i % 6 + 1)).text(),
                    "cclass" : $("#table-cclass" + parseInt(i / 6) + "-" + (i % 6 + 1)).text()
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
    });
    
    $('#sch-search').click(function(event) {
        $('#sch-result').fadeIn();
    });
    
    $('#sch-result .button').click(function(event) {
        $('#sch-result').fadeOut(100);
    });
		
    $('#sch-search').click(function(){

        $.ajax(
            { url : "/mysite2/Schedule/",
              data : {'major' : $('#major').val(),
                      'category': $('#category').val(),
                      'SearchName': $('#SearchName').val(),
                      'Page': "0"
                    },
              type : "POST",
              success:function(resp){  
                  $('#sch-search-result').html(resp);
    
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });
        $("#sch-result").hide();

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
                  $('#sch-search-result').html(resp);
                     
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
       
                  $('#sch-search-result').html(resp);
                   
                      
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
                  $('#sch-search-result').html(resp);
               
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });
});