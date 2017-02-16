$('#sch-result .button').click(function(event) {
        event.stopPropagation();
        $(this).unbind("click");
        $('#sch-result').fadeOut(100);
    });
    $('#sch-search-result .button').click(function(event) {
       event.stopPropagation();
        $(this).unbind("click");
        $('#sch-search-result').fadeOut(100);
    });
    $("div").on("click",'#sch-search',function(event){
        event.stopPropagation();
        $(this).unbind("click");
        $.ajax(
            { url : "/Schedule/",
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

    });
  