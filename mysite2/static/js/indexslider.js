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
for(var i=1; i<=10; i++)
{
    for(var j=1; j<=5;j++)
    {
        $('#sl'+i+''+j).slider();
        $('#sa'+i+''+j).slider();
        $('#sk'+i+''+j).slider();
        $('#sl'+i+''+j).slider('disable');
        $('#sa'+i+''+j).slider('disable');
        $('#sk'+i+''+j).slider('disable');
    }
}



$("[data-toggle=tooltip]").tooltip();

});