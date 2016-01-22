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

var sl1 = $('#sl1').slider(),
    sl2 = $('#sl2').slider(),
    sl3 = $('#sl3').slider(),
    sl4 = $('#sl4').slider(),
    sl5 = $('#sl5').slider(),
    sl6 = $('#sl6').slider();

$('#sl1').slider('disable');
$('#sl2').slider('disable');
$('#sl3').slider('disable');
$('#sl4').slider('disable');
$('#sl5').slider('disable');
$('#sl6').slider('disable');


var sl01 = $('#sl01').slider(),
    sl02 = $('#sl02').slider(),
    sl03 = $('#sl03').slider(),
    sl04 = $('#sl04').slider(),
    sl05 = $('#sl05').slider(),
    sl06 = $('#sl06').slider();

$('#sl01').slider('disable');
$('#sl02').slider('disable');
$('#sl03').slider('disable');
$('#sl04').slider('disable');
$('#sl05').slider('disable');
$('#sl06').slider('disable');


var sl11 = $('#sl11').slider(),
    sl12 = $('#sl12').slider(),
    sl13 = $('#sl13').slider(),
    sl14 = $('#sl14').slider(),
    sl15 = $('#sl15').slider(),
    sl16 = $('#sl16').slider();

$('#sl11').slider('disable');
$('#sl12').slider('disable');
$('#sl13').slider('disable');
$('#sl14').slider('disable');
$('#sl15').slider('disable');
$('#sl16').slider('disable');

var sl21 = $('#sl21').slider(),
    sl22 = $('#sl22').slider(),
    sl23 = $('#sl23').slider(),
    sl24 = $('#sl24').slider(),
    sl25 = $('#sl25').slider(),
    sl26 = $('#sl26').slider();
$('#sl21').slider('disable');
$('#sl22').slider('disable');
$('#sl23').slider('disable');
$('#sl24').slider('disable');
$('#sl25').slider('disable');
$('#sl26').slider('disable');

var sl31 = $('#sl31').slider(),
    sl32 = $('#sl32').slider(),
    sl33 = $('#sl33').slider(),
    sl34 = $('#sl34').slider(),
    sl35 = $('#sl35').slider(),
    sl36 = $('#sl36').slider();

$('#sl31').slider('disable');
$('#sl32').slider('disable');
$('#sl33').slider('disable');
$('#sl34').slider('disable');
$('#sl35').slider('disable');
$('#sl36').slider('disable');



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

          var CurrentPage=$(this).parent().attr("id")
          var url = location.href;
          var lastIndex = url.lastIndexOf('/');
          var cURL = url.substring(lastIndex);
        $('div').on('click',"#CoursePrevious",function(event){
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
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          
          });});  


        $('div').on('click',"#CoursePageNumber",function(event){
          event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

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
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          
          });
});

        $('div').on('click',"#CourseNext",function(event){
          event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

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
                        alert("좋아하는 강의로 등록 되었습니다.")
                      },
                      error: function(xhr, option, error){
                        alert(xhr.status); //오류코드
                        alert(error); //오류내용

                        } 
                  
                
                });

});
          
        });
