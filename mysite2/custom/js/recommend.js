$(document).ready(function(){
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

var sl1 = $('#sl1').slider(),
    sl2 = $('#sl2').slider(),
    sl3 = $('#sl3').slider();
    
$("[data-toggle=tooltip]").tooltip();


var checked = ['True', 'True', 'True', 'True', 'True', 'True'];

$('#enable1').on('click', function(){
  if(checked[0] == "False"){
    $('#sl1').slider('enable');
    $('#sl1').slider('setValue', 5);
    checked[0] = "True";
    $('#enable1').css('background-color', '#9acd32');
  } else {
    $('#sl1').slider('disable');
    $('#sl1').slider('setValue', 0);
    checked[0] = "False";
    $('#enable1').css('background-color', '#ccc');
  }
});

$('#enable2').on('click', function(){
  if(checked[1] == "False"){
    $('#sl2').slider('enable');
    $('#sl2').slider('setValue', 5);
    checked[1] = "True";
    $('#enable2').css('background-color', '#9acd32');
  } else {
    $('#sl2').slider('disable');
    $('#sl2').slider('setValue', 0);
    checked[1] = "False";
    $('#enable2').css('background-color', '#ccc');
  }
});

$('#enable3').on('click', function(){
  if(checked[2] == "False"){
    $('#sl3').slider('enable');
    $('#sl3').slider('setValue', 5);
    checked[2] = "True";
    $('#enable3').css('background-color', '#9acd32');
  } else {
    $('#sl3').slider('disable');
    $('#sl3').slider('setValue', 0);
    checked[2] = "False";
    $('#enable3').css('background-color', '#ccc');
  }
});

$('#enable6').on('click', function(){
  if($('#ButtonCheck').val() == "True"){
    $('#ButtonCheck').val("False")
    $('#enable6').css('background-color', '#ccc');
  } else {
    $('#ButtonCheck').val("True")
    $('#enable6').css('background-color', '#FFEB3B');
  }
});


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

  $('.stars').on("click", "input",function(event){
    event.stopPropagation();
    $(this).unbind("click");
    var splitdata = $(this).attr("id");
    splitdata = splitdata.split("-");
    var starcount = splitdata[1];
    $("#StarValue").val(starcount);
  });

  $("#recommend_form").submit(function(){

    var HSemester = $("#HSemester").val();
    var paper_value =$(".paper_value");
    var course_value =$(".course_value");

    var CourseComment = $("#CourseComment").val().length;
    var StarValue = $("#StarValue").val();

    var paper_length=paper_value.length;
    
    var course_length=course_value.length;
    
    var paper_result=0;
    var course_result=0;
    for(var i=0; i<paper_length; i++)
    {
        if($(paper_value).eq(i).val()!="0")
        {
          paper_result++;
        }
        
    }
    for(var i=0; i<course_length; i++)
    {
         if($(course_value).eq(i).val()!="0")
        {
          course_result++;
        }
        
    }
    //check if there is nothing
    if(HSemester == "0" || HSemester == ""){
      window.scrollTo(0, 200);
      alert("Please select the semester.");
      $("#text_semester").css("border", "2px solid red");
      return false;
    } 
    else if(CourseComment<300)
    {
      alert("comment의 길이는 300자 이상 이어야 합니다.(현재 글자 :"+CourseComment+")");
      return false;
    }
    else if(paper_result==0)
    {
      alert("시험방식을 선택 하지 않으셨습니다.");
      return false;
    }
    else if(course_result==0)
    {
      alert("수업방식을 선택 하지 않으셨습니다.");
      return false;
    }
    else if(StarValue==0)
    {
      alert("별점 0점은 줄 수 없습니다.");
      return false;
    }
    else
    {
      $('#recommend_form').attr({action:'/Recommend/Recommend_Write'})
    }
  });

  $("#Update_form").submit(function(){

    var HSemester = $("#HSemester").val();
    var paper_value =$(".paper_value");
    var course_value =$(".course_value");
    var CourseComment = $("#CourseComment").val().length;
    var StarValue = $("#StarValue").val();
    //check if there is nothing

    var paper_length=paper_value.length;
    
    var course_length=course_value.length;
    
    var paper_result=0;
    var course_result=0;
    for(var i=0; i<paper_length; i++)
    {
        if($(paper_value).eq(i).val()!="0")
        {
          paper_result++;
        }

    }
    for(var i=0; i<course_length; i++)
    {
         if($(course_value).eq(i).val()!="0")
        {
          course_result++;
        }
        
    }

    if(HSemester == "0" || HSemester == ""){
      window.scrollTo(0, 200);
      alert("Please select the semester.");
      $("#text_semester").css("border", "2px solid red");
      return false;
    } 
    else if(CourseComment<200)
    {
      alert("comment의 길이는 200자 이상 이어야 합니다.");
      return false;
    }
    else if(paper_result==0)
    {
      alert("시험방식을 선택 하지 않으셨습니다.");
      return false;
    }
    else if(course_result==0)
    {
      alert("수업방식을 선택 하지 않으셨습니다.");
      return false;
    }
    else if(StarValue==0)
    {
      alert("별점 0점은 줄 수 없습니다.");
      return false;
    }

    else
    {
      $('#Update_form').attr({action:'/UpdateWrite/'})
    }
  });
});


$(document).ready(function(){

  $('div').on("click",".paper_button",function()
  {
     event.stopPropagation();
    if($(this).text() =="해당없음")
    {
      if($(this).hasClass("active"))
      {
        $(this).removeClass('active');
        $(this).next().val("0");
      }
      else 
      {
        $('.paper_button').removeClass("active");
        
        $(this).addClass("active");
        $(".paper_value").val("0");
        $(this).next().val($(this).val())
      }

    }
    else if($(this).text()!="해당없음")
    {
       
        if($(this).hasClass("active"))
        {
          $(this).removeClass('active');
          $(this).next().val("0");
        }
        else 
        {
          $(this).addClass("active");
          $(this).next().val($(this).val());
           $(".paper_button").eq(3).removeClass("active")
         $(".paper_button").eq(3).next().val("0")
        }
       
    }
  });
   $('div').on("click",".course_button",function()
  {
     event.stopPropagation();
    if($(this).hasClass("active"))
    {
      $(this).removeClass('active');
      $(this).next().val("0");
    }
    else 
    {
      $(this).addClass("active");
       $(this).next().val($(this).val());
    }
    
  });
});

$(document).ready(function(){
  var max_fields = 10; //maximum input boxes allowed
  var wrapper = $(".input_fields_wrap"); //Fields wrapper
  var add_button = $(".add_field_button"); //Add button ID
  var add_div = $(".add").next().next();
  $(add_div).after("<a class='remove_field' style='cursor:pointer; font-size:13px; color:red;'>Del</a>");
  var x = 1; //initlal text box count
  $(add_button).on('click', function(){
  //on add input button click
      if(x < max_fields){ //max input box allowed
          x++; //text box increment
          $(wrapper).append('<div class="polymer-form dirty" style="margin-top:20px; margin-bottom:50px;"><input type="text" name="mytext[]" class="demo-form"><label class="placeholder" style="color: rgb(153, 153, 153);">문제 추가 &nbsp;</label><div class="bar" style="height: 2px; background-color: rgb(170, 170, 170);"></div><a class="remove_field" style="cursor:pointer; font-size:13px; color:red;">Del</a></div>'); //add input box
      }
      else
        alert("최대 10개까지 등록이 가능합니다.");
  });
  
  $(wrapper).on("click",".remove_field", function(){ //user click on remove text
      $(this).parent('div').remove(); x--;
  });
});