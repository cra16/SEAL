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

var sa11 = $('#sa11').slider(),
    sa12 = $('#sa12').slider(),
    sa13 = $('#sa13').slider(),
    sa14 = $('#sa14').slider(),
    sa21 = $('#sa21').slider(),
    sa22 = $('#sa22').slider(),
    sa23 = $('#sa23').slider(),
    sa24 = $('#sa24').slider(),
    sa31 = $('#sa31').slider(),
    sa32 = $('#sa32').slider(),
    sa33 = $('#sa33').slider(),
    sa34 = $('#sa34').slider(),
    sa41 = $('#sa41').slider(),
    sa42 = $('#sa42').slider(),
    sa43 = $('#sa43').slider(),
    sa44 = $('#sa44').slider(),
    sa51 = $('#sa51').slider(),
    sa52 = $('#sa52').slider(),
    sa53 = $('#sa53').slider(),
    sa54 = $('#sa54').slider(),
    sa61 = $('#sa61').slider(),
    sa62 = $('#sa62').slider(),
    sa63 = $('#sa63').slider(),
    sa64 = $('#sa64').slider(),
    sa71 = $('#sa71').slider(),
    sa72 = $('#sa72').slider(),
    sa73 = $('#sa73').slider(),
    sa74 = $('#sa74').slider();

var sk11 = $('#sk11').slider(),
    sk12 = $('#sk12').slider(),
    sk13 = $('#sk13').slider(),
    sk14 = $('#sk14').slider(),
    sk21 = $('#sk21').slider(),
    sk22 = $('#sk22').slider(),
    sk23 = $('#sk23').slider(),
    sk24 = $('#sk24').slider(),
    sk31 = $('#sk31').slider(),
    sk32 = $('#sk32').slider(),
    sk33 = $('#sk33').slider(),
    sk34 = $('#sk34').slider(),
    sk41 = $('#sk41').slider(),
    sk42 = $('#sk42').slider(),
    sk43 = $('#sk43').slider(),
    sk44 = $('#sk44').slider(),
    sk51 = $('#sk51').slider(),
    sk52 = $('#sk52').slider(),
    sk53 = $('#sk53').slider(),
    sk54 = $('#sk54').slider(),
    sk61 = $('#sk61').slider(),
    sk62 = $('#sk62').slider(),
    sk63 = $('#sk63').slider(),
    sk64 = $('#sk64').slider(),
    sk71 = $('#sk71').slider(),
    sk72 = $('#sk72').slider(),
    sk73 = $('#sk73').slider(),
    sk74 = $('#sk74').slider();

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

$('#sa11').slider('disable');
$('#sa12').slider('disable');
$('#sa13').slider('disable');
$('#sa14').slider('disable');
$('#sa21').slider('disable');
$('#sa22').slider('disable');
$('#sa23').slider('disable');
$('#sa24').slider('disable');
$('#sa31').slider('disable');
$('#sa32').slider('disable');
$('#sa33').slider('disable');
$('#sa34').slider('disable');
$('#sa41').slider('disable');
$('#sa42').slider('disable');
$('#sa43').slider('disable');
$('#sa44').slider('disable');
$('#sa51').slider('disable');
$('#sa52').slider('disable');
$('#sa53').slider('disable');
$('#sa54').slider('disable');
$('#sa61').slider('disable');
$('#sa62').slider('disable');
$('#sa63').slider('disable');
$('#sa64').slider('disable');
$('#sa71').slider('disable');
$('#sa72').slider('disable');
$('#sa73').slider('disable');
$('#sa74').slider('disable');

$('#sk11').slider('disable');
$('#sk12').slider('disable');
$('#sk13').slider('disable');
$('#sk14').slider('disable');
$('#sk21').slider('disable');
$('#sk22').slider('disable');
$('#sk23').slider('disable');
$('#sk24').slider('disable');
$('#sk31').slider('disable');
$('#sk32').slider('disable');
$('#sk33').slider('disable');
$('#sk34').slider('disable');
$('#sk41').slider('disable');
$('#sk42').slider('disable');
$('#sk43').slider('disable');
$('#sk44').slider('disable');
$('#sk51').slider('disable');
$('#sk52').slider('disable');
$('#sk53').slider('disable');
$('#sk54').slider('disable');
$('#sk61').slider('disable');
$('#sk62').slider('disable');
$('#sk63').slider('disable');
$('#sk64').slider('disable');
$('#sk71').slider('disable');
$('#sk72').slider('disable');
$('#sk73').slider('disable');
$('#sk74').slider('disable');



$("[data-toggle=tooltip]").tooltip();






});
