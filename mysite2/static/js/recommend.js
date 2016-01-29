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

var sl1 = $('#sl1').slider(),
    sl2 = $('#sl2').slider(),
    sl3 = $('#sl3').slider(),
    sl4 = $('#sl4').slider(),
    sl5 = $('#sl5').slider(),
    sl6 = $('#sl6').slider();

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

$('#enable4').on('click', function(){
  if(checked[3] == "False"){
    $('#sl4').slider('enable');
    $('#sl4').slider('setValue', 5);
    checked[3] = "True";
    $('#enable4').css('background-color', '#9acd32');
  } else {
    $('#sl4').slider('disable');
    $('#sl4').slider('setValue', 0);
    checked[3] = "False";
    $('#enable4').css('background-color', '#ccc');
  }
});

$('#enable5').on('click', function(){
  if(checked[4] == "False"){
    $('#sl5').slider('enable');
    $('#sl5').slider('setValue', 5);
    checked[4] = "True";
    $('#enable5').css('background-color', '#9acd32');
  } else {
    $('#sl5').slider('disable');
    $('#sl5').slider('setValue', 0);
    checked[4] = "False";
    $('#enable5').css('background-color', '#ccc');
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

});

$(document).ready(function(){
  $('.stars').on("click", "input",function(event){
    event.stopPropagation();
    $(this).unbind("click");
    var splitdata = $(this).attr("id");
    splitdata = splitdata.split("-");
    var starcount = splitdata[1];
    $("#StarValue").val(starcount);
  });

$("#recommend_form").submit(function(){
    var Hsemester = $("#HSemester").val();
    //check if there is nothing
    if(Hsemester == "0" || Hsemester == ""){
      window.scrollTo(0, 50);
      alert("Please select the semester.");
      $("#dropdown_semester").css("border", "2px solid red");
      $("#dropdown_semester").css("box-shadow", "0 0 3px red");
      return false;
    } else {
      $('#recommend_form').attr({action:'/Recommend/Recommend_Write'}).submit();
    }
  });

 });
