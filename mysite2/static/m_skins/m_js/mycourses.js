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

var sl1 = $('#sl11').slider(),
    sl2 = $('#sl12').slider(),
    sl3 = $('#sl13').slider(),
    sl4 = $('#sl14').slider(),
    sl5 = $('#sl21').slider(),
    sl6 = $('#sl22').slider(),
    sl7 = $('#sl23').slider(),
    sl8 = $('#sl24').slider(),
    sl9 = $('#sl31').slider(),
    sl10 = $('#sl32').slider(),
    sl11 = $('#sl33').slider(),
    sl12 = $('#sl34').slider(),
    sl13 = $('#sl41').slider(),
    sl14 = $('#sl42').slider(),
    sl15 = $('#sl43').slider(),
    sl16 = $('#sl44').slider(),
    sl17 = $('#sl51').slider(),
    sl18 = $('#sl52').slider(),
    sl19 = $('#sl53').slider(),
    sl20 = $('#sl54').slider(),
    sl21 = $('#sl61').slider(),
    sl22 = $('#sl62').slider(),
    sl23 = $('#sl63').slider(),
    sl24 = $('#sl64').slider(),

    sl01 = $('#sl111').slider(),
    sl02 = $('#sl112').slider(),
    sl03 = $('#sl113').slider(),
    sl04 = $('#sl114').slider(),
    sl05 = $('#sl121').slider(),
    sl06 = $('#sl122').slider(),
    sl07 = $('#sl123').slider(),
    sl08 = $('#sl124').slider(),
    sl09 = $('#sl131').slider(),
    sl010 = $('#sl132').slider(),
    sl011 = $('#sl133').slider(),
    sl012 = $('#sl134').slider(),
    sl013 = $('#sl141').slider(),
    sl014 = $('#sl142').slider(),
    sl015 = $('#sl143').slider(),
    sl016 = $('#sl144').slider(),
    sl017 = $('#sl151').slider(),
    sl018 = $('#sl152').slider(),
    sl019 = $('#sl153').slider(),
    sl020 = $('#sl154').slider(),
    sl021 = $('#sl161').slider(),
    sl022 = $('#sl162').slider(),
    sl023 = $('#sl163').slider(),
    sl024 = $('#sl164').slider();

$('#sl11').slider('disable');
$('#sl12').slider('disable');
$('#sl13').slider('disable');
$('#sl14').slider('disable');
$('#sl21').slider('disable');
$('#sl22').slider('disable');
$('#sl23').slider('disable');
$('#sl24').slider('disable');
$('#sl31').slider('disable');
$('#sl32').slider('disable');
$('#sl33').slider('disable');
$('#sl34').slider('disable');
$('#sl41').slider('disable');
$('#sl42').slider('disable');
$('#sl43').slider('disable');
$('#sl44').slider('disable');
$('#sl51').slider('disable');
$('#sl52').slider('disable');
$('#sl53').slider('disable');
$('#sl54').slider('disable');
$('#sl61').slider('disable');
$('#sl62').slider('disable');
$('#sl63').slider('disable');
$('#sl64').slider('disable');

$('#sl111').slider('disable');
$('#sl112').slider('disable');
$('#sl113').slider('disable');
$('#sl114').slider('disable');
$('#sl121').slider('disable');
$('#sl122').slider('disable');
$('#sl123').slider('disable');
$('#sl124').slider('disable');
$('#sl131').slider('disable');
$('#sl132').slider('disable');
$('#sl133').slider('disable');
$('#sl134').slider('disable');
$('#sl141').slider('disable');
$('#sl142').slider('disable');
$('#sl143').slider('disable');
$('#sl144').slider('disable');
$('#sl151').slider('disable');
$('#sl152').slider('disable');
$('#sl153').slider('disable');
$('#sl154').slider('disable');
$('#sl161').slider('disable');
$('#sl162').slider('disable');
$('#sl163').slider('disable');
$('#sl164').slider('disable');


$("[data-toggle=tooltip]").tooltip();



 $('div').on('click',"#LikePage",function(event){
          event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

        $.ajax(
            { url : "/mysite2/MyCoursePage/",
              data : {'Page': $(this).attr("name"),
                      'CurrentPage':CurrentPage
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
                        $('#LikePageMain').html(resp);
                 },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          
          });

     



    });

    $('div').on('click','#LikeNext',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

        $.ajax(
            { url : "/mysite2/MyCoursePage/",
              data : {'Page': $(this).attr("name"),
                      'CurrentPage':CurrentPage
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
                    $('#LikePageMain').html(resp);
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });

   $('div').on('click','#LikePrevious',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

        $.ajax(
            { url : "/mysite2/MyCoursePage/",
              data : {'Page': $(this).attr("name"),
                      'CurrentPage':CurrentPage
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
              $('#LikePageMain').html(resp);
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });






 $('div').on('click',"#RecommendPage",function(event){
          event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

        $.ajax(
            { url : "/mysite2/MyCoursePage/",
              data : {'Page': $(this).attr("name"),
                        'CurrentPage':CurrentPage
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
                  $('#RecommendPageMain').html(resp);
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          
          });

     



    });

    $('div').on('click','#RecommendNext',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

        $.ajax(
            { url : "/mysite2/MyCoursePage/",
              data : {'Page': $(this).attr("name"),
                      'CurrentPage':CurrentPage
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
               $('#RecommendPageMain').html(resp);
                
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });

    $('div').on('click','#RecommendPrevious',function(){
        event.stopPropagation();
          $(this).unbind("click");
          var CurrentPage=$(this).parent().attr("id")

         $.ajax(
            { url : "/mysite2/MyCoursePage/",
              data : {'Page': $(this).attr("name"),
                    'CurrentPage':CurrentPage
                    },
              
              datatype:"json",
              type : "POST",
              async:true,
              success:function(resp){     
               $('#RecommendPageMain').html(resp);
                
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });



    });
});