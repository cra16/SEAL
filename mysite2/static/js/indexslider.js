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

var sl1 = $('#sl11').slider();
var sl2 = $('#sl12').slider();
var sl3 = $('#sl13').slider();
var sl4 = $('#sl14').slider();

$('#sl11').slider('disable');
$('#sl12').slider('disable');
$('#sl13').slider('disable');
$('#sl14').slider('disable');

$('#sl11').slider('setValue', 5);
$('#sl12').slider('setValue', 5);
$('#sl13').slider('setValue', 5);
$('#sl14').slider('setValue', 5);

$("[data-toggle=tooltip]").tooltip();


var	ccode = document.getElementsByName('ccode')
var cname = document.getElementsByName('cname')
var cprof = document.getElementsByName('cprof')

var likenum1 = 120;
   

var eccode1 = document.getElementsByName('ccode')[0];
var ecname1 = document.getElementsByName('cname')[1];
var ecprof1 = document.getElementsByName('cprof')[2];

var elikenum1 = document.getElementById('likenum1');

eccode1.textContent = ccode[0].value;
ecname1.textContent = cname[1];
ecprof1.textContent = "후";

elikenum1.textContent = likenum1;
});
