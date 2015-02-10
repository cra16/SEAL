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

$(function(){
              $("[data-toggle=tooltip]").tooltip();
            });
            $('#recommendbtn_d').on('click', function(){
              var data1 = $('#sl1').data('slider').getValue(),
                  data2 = $('#sl2').data('slider').getValue(),
                  data3 = $('#sl3').data('slider').getValue(),
                  data4 = $('#sl4').data('slider').getValue(),
                  data5 = $('#sl5').data('slider').getValue(),
                  data6 = $('#sl6').data('slider').getValue();
            });	

$('#enable1').click(function(){$('#sl1').slider('enable')});
$('#disable1').click(function(){$('#sl1').slider('disable')});
$('#enable2').click(function(){$('#sl2').slider('enable')});
$('#disable2').click(function(){$('#sl2').slider('disable')});
$('#enable3').click(function(){$('#sl3').slider('enable')});
$('#disable3').click(function(){$('#sl3').slider('disable')});
$('#enable4').click(function(){$('#sl4').slider('enable')});
$('#disable4').click(function(){$('#sl4').slider('disable')});
$('#enable5').click(function(){$('#sl5').slider('enable')});
$('#disable5').click(function(){$('#sl5').slider('disable')});
$('#enable6').click(function(){$('#sl6').slider('enable')});
$('#disable6').click(function(){$('#sl6').slider('disable')});

$('#disable1').on('click', function(){$('#sl1').slider('setValue', 5);});
$('#disable2').on('click', function(){$('#sl2').slider('setValue', 5);});
$('#disable3').on('click', function(){$('#sl3').slider('setValue', 5);});
$('#disable4').on('click', function(){$('#sl4').slider('setValue', 5);});
$('#disable5').on('click', function(){$('#sl5').slider('setValue', 5);});
$('#disable6').on('click', function(){$('#sl6').slider('setValue', 5);});


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
