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

$('#recommendbtn_d').on('click', function(){
  var data1 = $('#sl1').data('slider').getValue(),
      data2 = $('#sl2').data('slider').getValue(),
      data3 = $('#sl3').data('slider').getValue(),
      data4 = $('#sl4').data('slider').getValue(),
      data5 = $('#sl5').data('slider').getValue(),
      data6 = $('#sl6').data('slider').getValue();

  $.post("../recommend.php", {data1: data1, data2: data2, data3: data3, data4: data4, data5: data5, data6: data6}, function(data){
    if(data == 0){
      alert("Touroku failed");
    }
    else{
      alert(data);
      window.location.href = "../html/index.html"
    }
  });
});

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
  if(checked[5] == "False"){
    $('#sl6').slider('enable');
    $('#sl6').slider('setValue', 5);
    checked[5] = "True";
    $('#enable6').css('background-color', '#9acd32');
  } else {
    $('#sl6').slider('disable');
    $('#sl6').slider('setValue', 0);
    checked[5] = "False";
    $('#enable6').css('background-color', '#ccc');
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

elikenum1.textContent = likenum1;

});
