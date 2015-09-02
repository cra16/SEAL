$(document).ready(function(event) {
    
    $('#submit_qna').click(function() {
        alert("작성한 글이 등록되었습니다.");
    });
    
    $('div').on('click',"#Page",function(event){
          event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

        $.ajax(
            { url : "/QnA/Page/",
              data : {'Page': $(this).attr("name"),
           
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
                  $('#QnA_List').html(resp);
                  
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용0

                  } 
            
          
          });

     



    });

    $('div').on('click','#Next',function(event){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

        $.ajax(
            { url : "/QnA/Page/",
              data : {'Page': $(this).attr("name"),
     
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
             		 $('#QnA_List').html(resp);
                  
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });

    $('div').on('click','#Previous',function(event){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

        $.ajax(
            { url : "/QnA/Page/",
              data : {'Page': $(this).attr("name"),
      
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){
                       $('#QnA_List').html(resp);
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });
});