$(document).ready(function() {
    // schedule_table javascript
    $('.table td').css( 'cursor', 'pointer' );
    
    var arr=['월', '화', '수', '목', '금', '토'];
    
    $("div").on("click",'.table td',function(event) {
      event.stopPropagation();
      if(confirm((arr[$(this).index()-1]) + "요일 " + ($(this).parent().index()+1) + "교시 수업을 검색하시겠습니까?")==true){
          // $('#sch-result').fadeIn();
          var link_page = '/mysite2/sel_period/' + (arr[$(this).index()-1]) + ($(this).parent().index()+1)  + "_/" + 1 + "/";
          $.ajax(
            { url : link_page,
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
        };
    });

    $("#table").find("td").each(function(i, e){
          $(this).unbind("click");
      $("#del-my-lec" + parseInt(i / 6) + "-" + (i % 6 + 1)).click(function(event){
        event.stopPropagation();
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

})
