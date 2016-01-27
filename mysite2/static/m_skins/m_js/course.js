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

var sl11 = $('#sl11').slider(),
    sl12 = $('#sl12').slider(),
    sl13 = $('#sl13').slider(),
    sl14 = $('#sl14').slider(),
    sl15 = $('#sl15').slider(),
    sl21 = $('#sl21').slider(),
    sl22 = $('#sl22').slider(),
    sl23 = $('#sl23').slider(),
    sl24 = $('#sl24').slider(),
    sl25 = $('#sl25').slider(),
    sl31 = $('#sl31').slider(),
    sl32 = $('#sl32').slider(),
    sl33 = $('#sl33').slider(),
    sl34 = $('#sl34').slider(),
    sl35 = $('#sl35').slider(),
    sl41 = $('#sl41').slider(),
    sl42 = $('#sl42').slider(),
    sl43 = $('#sl43').slider(),
    sl44 = $('#sl44').slider(),
    sl45 = $('#sl45').slider(),
    sl51 = $('#sl51').slider(),
    sl52 = $('#sl52').slider(),
    sl53 = $('#sl53').slider(),
    sl54 = $('#sl54').slider(),
    sl55 = $('#sl55').slider(),
    sl61 = $('#sl61').slider(),
    sl62 = $('#sl62').slider(),
    sl63 = $('#sl63').slider(),
    sl64 = $('#sl64').slider(),
    sl65 = $('#sl65').slider(),  
    sl71 = $('#sl71').slider(),
    sl72 = $('#sl72').slider(),
    sl73 = $('#sl73').slider(),
    sl74 = $('#sl74').slider(),
    sl75 = $('#sl75').slider(),
    sl81 = $('#sl81').slider(),
    sl82 = $('#sl82').slider(),
    sl83 = $('#sl83').slider(),
    sl84 = $('#sl84').slider(),
    sl85 = $('#sl85').slider(),
    sl91 = $('#sl91').slider(),
    sl92 = $('#sl92').slider(),
    sl93 = $('#sl93').slider(),
    sl94 = $('#sl94').slider(),
    sl95 = $('#sl95').slider(),
    sl101 = $('#sl101').slider(),
    sl102 = $('#sl102').slider(),
    sl103 = $('#sl103').slider(),
    sl104 = $('#sl104').slider(),
    sl105 = $('#sl105').slider();


var sa11 = $('#sa11').slider(),
    sa12 = $('#sa12').slider(),
    sa13 = $('#sa13').slider(),
    sa14 = $('#sa14').slider(),      
    sa15 = $('#sa15').slider(),
    sa21 = $('#sa21').slider(),
    sa22 = $('#sa22').slider(),
    sa23 = $('#sa23').slider(),
    sa24 = $('#sa24').slider(),
    sa25 = $('#sa25').slider(),
    sa31 = $('#sa31').slider(),
    sa32 = $('#sa32').slider(),
    sa33 = $('#sa33').slider(),
    sa34 = $('#sa34').slider(),
    sa35 = $('#sa35').slider(),
    sa41 = $('#sa41').slider(),
    sa42 = $('#sa42').slider(),
    sa43 = $('#sa43').slider(),
    sa44 = $('#sa44').slider(),
    sa45 = $('#sa45').slider(),
    sa51 = $('#sa51').slider(),
    sa52 = $('#sa52').slider(),
    sa53 = $('#sa53').slider(),
    sa54 = $('#sa54').slider(),
    sa55 = $('#sa55').slider(),
    sa61 = $('#sa61').slider(),
    sa62 = $('#sa62').slider(),
    sa63 = $('#sa63').slider(),
    sa64 = $('#sa64').slider(),
    sa65 = $('#sa65').slider(),

    sa71 = $('#sa71').slider(),
    sa72 = $('#sa72').slider(),
    sa73 = $('#sa73').slider(),
    sa74 = $('#sa74').slider(),
    sa75 = $('#sa75').slider(),
    sa81 = $('#sa81').slider(),
    sa82 = $('#sa82').slider(),
    sa83 = $('#sa83').slider(),
    sa84 = $('#sa84').slider(),
    sa85 = $('#sa85').slider(),
    sa91 = $('#sa91').slider(),
    sa92 = $('#sa92').slider(),
    sa93 = $('#sa93').slider(),
    sa94 = $('#sa94').slider(),
    sa95 = $('#sa95').slider(),
    sa101 = $('#sa101').slider(),
    sa102 = $('#sa102').slider(),
    sa103 = $('#sa103').slider(),
    sa104 = $('#sa104').slider(),
    sa105 = $('#sa105').slider();

$('#sl11').slider('disable');
$('#sl12').slider('disable');
$('#sl13').slider('disable');
$('#sl14').slider('disable');
$('#sl15').slider('disable');
$('#sl21').slider('disable');
$('#sl22').slider('disable');
$('#sl23').slider('disable');
$('#sl24').slider('disable');
$('#sl25').slider('disable');
$('#sl31').slider('disable');
$('#sl32').slider('disable');
$('#sl33').slider('disable');
$('#sl34').slider('disable');
$('#sl35').slider('disable');
$('#sl41').slider('disable');
$('#sl42').slider('disable');
$('#sl43').slider('disable');
$('#sl44').slider('disable');
$('#sl45').slider('disable');
$('#sl51').slider('disable');
$('#sl52').slider('disable');
$('#sl53').slider('disable');
$('#sl54').slider('disable');
$('#sl55').slider('disable');
$('#sl61').slider('disable');
$('#sl62').slider('disable');
$('#sl63').slider('disable');
$('#sl64').slider('disable');
$('#sl65').slider('disable');
$('#sl71').slider('disable');
$('#sl72').slider('disable');
$('#sl73').slider('disable');
$('#sl74').slider('disable');
$('#sl75').slider('disable');
$('#sl81').slider('disable');
$('#sl82').slider('disable');
$('#sl83').slider('disable');
$('#sl84').slider('disable');
$('#sl85').slider('disable');
$('#sl91').slider('disable');
$('#sl92').slider('disable');
$('#sl93').slider('disable');
$('#sl94').slider('disable');
$('#sl95').slider('disable');
$('#sl101').slider('disable');
$('#sl102').slider('disable');
$('#sl103').slider('disable');
$('#sl104').slider('disable');
$('#sl105').slider('disable');

$('#sa11').slider('disable');
$('#sa12').slider('disable');
$('#sa13').slider('disable');
$('#sa14').slider('disable');
$('#sa15').slider('disable');
$('#sa21').slider('disable');
$('#sa22').slider('disable');
$('#sa23').slider('disable');
$('#sa24').slider('disable');
$('#sa25').slider('disable');
$('#sa31').slider('disable');
$('#sa32').slider('disable');
$('#sa33').slider('disable');
$('#sa34').slider('disable');
$('#sa35').slider('disable');
$('#sa41').slider('disable');
$('#sa42').slider('disable');
$('#sa43').slider('disable');
$('#sa44').slider('disable');
$('#sa45').slider('disable');
$('#sa51').slider('disable');
$('#sa52').slider('disable');
$('#sa53').slider('disable');
$('#sa54').slider('disable');
$('#sa55').slider('disable');
$('#sa61').slider('disable');
$('#sa62').slider('disable');
$('#sa63').slider('disable');
$('#sa64').slider('disable');
$('#sa65').slider('disable');
$('#sa71').slider('disable');
$('#sa72').slider('disable');
$('#sa73').slider('disable');
$('#sa74').slider('disable');
$('#sa75').slider('disable');
$('#sa81').slider('disable');
$('#sa82').slider('disable');
$('#sa83').slider('disable');
$('#sa84').slider('disable');
$('#sa85').slider('disable');
$('#sa91').slider('disable');
$('#sa92').slider('disable');
$('#sa93').slider('disable');
$('#sa94').slider('disable');
$('#sa95').slider('disable');
$('#sa101').slider('disable');
$('#sa102').slider('disable');
$('#sa103').slider('disable');
$('#sa104').slider('disable');
$('#sa105').slider('disable');


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



var ccode = document.getElementsByName('ccode')
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

        $('div').on('click',"#CoursePageNext",function(event){
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
                        alert("듣고 싶은 강의로 등록 되었습니다.")
                      },
                      error: function(xhr, option, error){
                        alert(xhr.status); //오류코드
                        alert(error); //오류내용

                        } 
                  
                
                });

});
          
        });
