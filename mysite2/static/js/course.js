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

$('#sl1').slider('setValue', 5);
$('#sl2').slider('setValue', 5);
$('#sl3').slider('setValue', 5);
$('#sl4').slider('setValue', 5);
$('#sl5').slider('setValue', 5);
$('#sl6').slider('setValue', 5);

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

$('#sl11').slider('setValue', 5);
$('#sl12').slider('setValue', 5);
$('#sl13').slider('setValue', 5);
$('#sl14').slider('setValue', 5);
$('#sl15').slider('setValue', 5);
$('#sl16').slider('setValue', 5);

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

$('#sl21').slider('setValue', 5);
$('#sl22').slider('setValue', 5);
$('#sl23').slider('setValue', 5);
$('#sl24').slider('setValue', 5);
$('#sl25').slider('setValue', 5);
$('#sl26').slider('setValue', 5);

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

$('#sl31').slider('setValue', 5);
$('#sl32').slider('setValue', 5);
$('#sl33').slider('setValue', 5);
$('#sl34').slider('setValue', 5);
$('#sl35').slider('setValue', 5);
$('#sl36').slider('setValue', 5);

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
$('#sl46').slider('disable');4

$('#sl41').slider('setValue', 5);
$('#sl42').slider('setValue', 5);
$('#sl43').slider('setValue', 5);
$('#sl44').slider('setValue', 5);
$('#sl45').slider('setValue', 5);
$('#sl46').slider('setValue', 5);

var sl51 = $('#sl51').slider(),
    sl52 = $('#sl52').slider(),
    sl53 = $('#sl53').slider(),
    sl54 = $('#sl54').slider(),
    sl55 = $('#sl55').slider(),
    sl56 = $('#sl56').slider();

$('#sl51').slider('disable');
$('#sl52').slider('disable');
$('#sl53').slider('disable');
$('#sl54').slider('disable');
$('#sl55').slider('disable');
$('#sl56').slider('disable');

$('#sl51').slider('setValue', 5);
$('#sl52').slider('setValue', 5);
$('#sl53').slider('setValue', 5);
$('#sl54').slider('setValue', 5);
$('#sl55').slider('setValue', 5);
$('#sl56').slider('setValue', 5);

var sl61 = $('#sl61').slider(),
    sl62 = $('#sl62').slider(),
    sl63 = $('#sl63').slider(),
    sl64 = $('#sl64').slider(),
    sl65 = $('#sl65').slider(),
    sl66 = $('#sl66').slider();

$('#sl61').slider('disable');
$('#sl62').slider('disable');
$('#sl63').slider('disable');
$('#sl64').slider('disable');
$('#sl65').slider('disable');
$('#sl66').slider('disable');

$('#sl61').slider('setValue', 5);
$('#sl62').slider('setValue', 5);
$('#sl63').slider('setValue', 5);
$('#sl64').slider('setValue', 5);
$('#sl65').slider('setValue', 5);
$('#sl66').slider('setValue', 5);

var ccode = "ECE20018",
    cname = "C 프로그래밍",
    cprof = "최창범 교수님";

var eccode = document.getElementById('ccode'),
    ecname = document.getElementById('cname'),
    ecprof = document.getElementById('cprof');

eccode.textContent = ccode;
ecname.textContent = cname;
ecprof.textContent = cprof;
});