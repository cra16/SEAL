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

var ccodeheader = document.getElementsByName('ccode');
var cnameheader = document.getElementByName('cname');
var cprofheader = document.getElementByName('cprof');
var ccode = new Array();
var cname = new Array();
var cporf = new Array();
for(var i =0; i< ccodeheader.length; i++)
{
	ccode[i] = document.getElementsByName('ccode')[i].value;
    cname[i] = document.getElementsByName('cname')[i].value;
    cprof[i] = document.getElementsByName('cprof')[i].value;
}
var likenum1 = 120;
   
var eccode1 = document.getElementByNames('ccode')[0].value.;
var ecname1 = document.getElementByNames('cname')[0].value;
var ecprof1 = document.getElementByNames('cprof')[0].vaule;

var elikenum1 = document.getElementById('likenum1');

eccode1.textContent = ccode1;
ecname1.textContent = cname1;
ecprof1.textContent = cprof1;

elikenum1.textContent = likenum1;
});
