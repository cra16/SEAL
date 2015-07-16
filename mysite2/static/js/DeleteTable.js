$(document).ready(function()
{
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