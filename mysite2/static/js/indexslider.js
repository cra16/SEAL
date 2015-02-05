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

var sl1 = $('#sl1').slider();
var sl2 = $('#sl2').slider();
var sl3 = $('#sl3').slider();
var sl4 = $('#sl4').slider();

$('#sl1').slider('disable');
$('#sl2').slider('disable');
$('#sl3').slider('disable');
$('#sl4').slider('disable');

$('#sl1').slider('setValue', 5);
$('#sl2').slider('setValue', 5);
$('#sl3').slider('setValue', 5);
$('#sl4').slider('setValue', 5);

$("[data-toggle=tooltip]").tooltip();


var	ccode = document.getElementsByName('ccode')
var cname = document.getElementsByName('cname')
var cprof = document.getElementsByName('cprof')

var likenum1 = 120;
   

var elikenum1 = document.getElementById('likenum1');


for(var i=0 i<ccode.length; i++)
{
	ccode[i].textContent = document.getElementsByName('ccode')[i].innerHTML
	cname[i].textContent = document.getElementsByName('cname')[i].innerHTML;
	cprof[i].textContent = document.getElementsByName('cprof')[i].innerHTML;
}

elikenum1.textContent = likenum1;
});
