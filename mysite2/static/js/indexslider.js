$(function()
{
	$.fn.slider.Constructor.prototype.disable = function () {this.picker.off();}
	$.fn.slider.Constructor.prototype.enable = function () 
	{
		if (this.touchCapable) 
		{
			// Touch: Bind touch events:
			this.picker.on(
				{
					touchstart: $.proxy(this.mousedown, this)
				});
		} else {
		this.picker.on({
			mousedown: $.proxy(this.mousedown, this)
						});
	 }
}

var sl1 = $('#sl11').slider(),
    sl2 = $('#sl12').slider(),
    sl3 = $('#sl13').slider(),
    sl4 = $('#sl14').slider();

$('#sl11').slider('disable');
$('#sl12').slider('disable');
$('#sl13').slider('disable');
$('#sl14').slider('disable');

$('#sl11').slider('setValue', 5);
$('#sl12').slider('setValue', 5);
$('#sl13').slider('setValue', 5);
$('#sl14').slider('setValue', 5);
$("[data-toggle=tooltip]").tooltip();

var ccode1 = "ECE20018",
    cname1 = "C 프로그래밍",
    cprof1 = "최창범 교수님",


    likenum1 = 120,

var eccode1 = document.getElementById('ccode1'),
    ecname1 = document.getElementById('cname1'),
    ecprof1 = document.getElementById('cprof1'),
             

    elikenum1 = document.getElementById('likenum1'),

eccode1.textContent = ccode1;
ecname1.textContent = cname1;
ecprof1.textContent = cprof1;


elikenum1.textContent = likenum1;
<<<<<<< HEAD
)};
=======
});
>>>>>>> darkzero1
