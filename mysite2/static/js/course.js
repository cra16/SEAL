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