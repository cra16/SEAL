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