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
   
var eccode1 = document.getElementByName('ccode');
var ecname1 = document.getElementByName('cname');
var ecprof1 = document.getElementByName('cprof');

var elikenum1 = document.getElementById('likenum1');

eccode1.textContent = ccode[0];
ecname1.textContent = cname[0];
ecprof1.textContent = cprof[0];

elikenum1.textContent = likenum1;
});
