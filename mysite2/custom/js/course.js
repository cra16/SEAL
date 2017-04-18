  $(function(){
  $.fn.slider.Constructor.prototype.disable = function () {this.picker.off();}
  $.fn.slider.Constructor.prototype.enable = function () {
    if (this.touchCapable) {
      // Touch: Bind touch events:
      this.picker.on({
        touchstart: $.proxy(this.mousedown, this)
      });
      } else {
        this.picker.on({
        mousedown: $.proxy(this.mousedown, this)
        });
      }
  }

  $("[data-toggle=tooltip]").tooltip();
  $(document).ready(function() {
  $(".ui.modal").modal("hide");
});



  for(var i=1; i<=10; i++)
  {
    for(var j=1; j<=5; j++)
    {
      $('#sl'+i+''+j).slider();
      $('#sa'+i+''+j).slider();
      $('#sl'+i+''+j).slider('disable');
      $('#sa'+i+''+j).slider('disable');
    }

  }


  for(var i=1; i<=6; i++)
  {
    $('#sl'+i).slider();
    $('#sl'+i).slider('disable');
  }

});
var	ccode = document.getElementsByName('ccode')
var cname = document.getElementsByName('cname')
var cprof = document.getElementsByName('cprof')

var likenum1 = 120;
   

var elikenum1 = document.getElementById('likenum1');


for(var i=0; i<ccode.length; i++)
{
	ccode[i].textContent = document.getElementsByName('ccode')[i].innerHTML;
	cname[i].textContent = document.getElementsByName('cname')[i].innerHTML;
	cprof[i].textContent = document.getElementsByName('cprof')[i].innerHTML;
}
$(window).load(function()
{


          var CurrentPage=$(this).parent().attr("id");
          var url = location.href;
          var lastIndex = url.lastIndexOf('/');
          var cURL = url.substring(lastIndex);
        

        $('div').on('click',"#CoursePagePrevious",function(event){
          event.stopPropagation();
          $(this).unbind("click");
  


        $.ajax(
            { url : "/CoursePageNation"+cURL,
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
                  $('#CoursePage').html(resp);
                  $.fn.initSlide();
                  $('span.starvalue').starvalue();
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          
          });

      });  


        $('div').on('click',"#CoursePageNumber",function(event){
          event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id");


        $.ajax(
            { url : "/CoursePageNation"+cURL,
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
                 $('#CoursePage').html(resp);
                 $.fn.initSlide();
                 $('span.starvalue').starvalue();
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          
          });



});

        $('div').on('click',"#CoursePageNext",function(event){
          event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id");

        $.ajax(
            { url : "/CoursePageNation"+cURL,
              data : {'Page': $(this).attr("name"),
                      'Current':CurrentPage
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
                  $('#CoursePage').html(resp);
                  $.fn.initSlide();
                  $('span.starvalue').starvalue();
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
            
          });


});

          $('div').on('click',"#listenButton",function(event){
             event.stopPropagation();
             $(this).unbind("click");
              var CurrentPage=$(this).attr("name")

              $.ajax(
                  { url : "/Like/",
                    data : {'Page': CurrentPage,
                          },
                    
                    datatype:"json",
                    type : "POST",
                    success:function(resp){     
                        alert("듣고 싶은 강의로 등록 되었습니다.")
                      },
                      error: function(xhr, option, error){
                        alert("이미 중복된 강의가 있습니다.");
                        } 
                  
                
                });
                
            });
        
           
});
