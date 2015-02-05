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

var sl11 = $('#sl11').slider(),
    sl12 = $('#sl12').slider(),
    sl13 = $('#sl13').slider(),
    sl14 = $('#sl14').slider(),
    sl21 = $('#sl21').slider(),
    sl22 = $('#sl22').slider(),
    sl23 = $('#sl23').slider(),
    sl24 = $('#sl24').slider(),
    sl31 = $('#sl31').slider(),
    sl32 = $('#sl32').slider(),
    sl33 = $('#sl33').slider(),
    sl34 = $('#sl34').slider(),
    sl41 = $('#sl41').slider(),
    sl42 = $('#sl42').slider(),
    sl43 = $('#sl43').slider(),
    sl44 = $('#sl44').slider(),
    sl51 = $('#sl51').slider(),
    sl52 = $('#sl52').slider(),
    sl53 = $('#sl53').slider(),
    sl54 = $('#sl54').slider(),
    sl61 = $('#sl61').slider(),
    sl62 = $('#sl62').slider(),
    sl63 = $('#sl63').slider(),
    sl64 = $('#sl64').slider(),
    sl71 = $('#sl71').slider(),
    sl72 = $('#sl72').slider(),
    sl73 = $('#sl73').slider(),
    sl74 = $('#sl74').slider();

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
$('#sl71').slider('disable');
$('#sl72').slider('disable');
$('#sl73').slider('disable');
$('#sl74').slider('disable');

$('#sl11').slider('setValue', 5);
$('#sl12').slider('setValue', 5);
$('#sl13').slider('setValue', 5);
$('#sl14').slider('setValue', 5);
$('#sl21').slider('setValue', 5);
$('#sl22').slider('setValue', 5);
$('#sl23').slider('setValue', 5);
$('#sl24').slider('setValue', 5);
$('#sl31').slider('setValue', 5);
$('#sl32').slider('setValue', 5);
$('#sl33').slider('setValue', 5);
$('#sl34').slider('setValue', 5);
$('#sl41').slider('setValue', 5);
$('#sl42').slider('setValue', 5);
$('#sl43').slider('setValue', 5);
$('#sl44').slider('setValue', 5);
$('#sl51').slider('setValue', 5);
$('#sl52').slider('setValue', 5);
$('#sl53').slider('setValue', 5);
$('#sl54').slider('setValue', 5);
$('#sl61').slider('setValue', 5);
$('#sl62').slider('setValue', 5);
$('#sl63').slider('setValue', 5);
$('#sl64').slider('setValue', 5);
$('#sl71').slider('setValue', 5);
$('#sl72').slider('setValue', 5);
$('#sl73').slider('setValue', 5);
$('#sl74').slider('setValue', 5);

$("[data-toggle=tooltip]").tooltip();


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
