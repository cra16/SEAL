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

var sl11 = $('#sl1').slider(),
    sl12 = $('#sl2').slider(),
    sl13 = $('#sl3').slider(),
    sl14 = $('#sl4').slider(),
    sl15 = $('#sl5').slider(),
    sl16 = $('#sl6').slider();

$('#sl1').slider('disable');
$('#sl2').slider('disable');
$('#sl3').slider('disable');
$('#sl4').slider('disable');
$('#sl5').slider('disable');
$('#sl6').slider('disable');


var sl1 = $('#sl11').slider(),
    sl2 = $('#sl12').slider(),
    sl3 = $('#sl13').slider(),
    sl4 = $('#sl14').slider(),
    sl5 = $('#sl15').slider(),
    sl6 = $('#sl16').slider();

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

var sl41 = $('#sl41').slider(),
    sl42 = $('#sl42').slider(),
    sl43 = $('#sl43').slider(),
    sl44 = $('#sl44').slider(),
    sl45 = $('#sl45').slider(),
    sl46 = $('#sl46').slider();

$('#sl41').slider('disable');
$('#sl42').slider('disable');
$('#sl43').slider('disable');
$('#sl44').slider('disable');
$('#sl45').slider('disable');
$('#sl46').slider('disable');



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

elikenum1.textContent = likenum1;
});