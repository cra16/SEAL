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

var sl1 = $('#sl11').slider(),
    sl2 = $('#sl12').slider(),
    sl3 = $('#sl13').slider(),
    sl4 = $('#sl14').slider(),
    sl5 = $('#sl21').slider(),
    sl6 = $('#sl22').slider(),
    sl7 = $('#sl23').slider(),
    sl8 = $('#sl24').slider(),
    sl9 = $('#sl31').slider(),
    sl10 = $('#sl32').slider(),
    sl11 = $('#sl33').slider(),
    sl12 = $('#sl34').slider(),
    sl13 = $('#sl41').slider(),
    sl14 = $('#sl42').slider(),
    sl15 = $('#sl43').slider(),
    sl16 = $('#sl44').slider(),
    sl17 = $('#sl51').slider(),
    sl18 = $('#sl52').slider(),
    sl19 = $('#sl53').slider(),
    sl20 = $('#sl54').slider(),
    sl21 = $('#sl61').slider(),
    sl22 = $('#sl62').slider(),
    sl23 = $('#sl63').slider(),
    sl24 = $('#sl64').slider(),
    sl25 = $('#sl71').slider(),
    sl26 = $('#sl72').slider(),
    sl27 = $('#sl73').slider(),
    sl28 = $('#sl74').slider();

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

var ccode1 = "ECE20018",
    cname1 = "C 프로그래밍",
    cprof1 = "최창범 교수님",

    ccode2 = "ECE20002",
    cname2 = "자바 프로그래밍",
    cprof2 = "김인중 교수님",

    ccode3 = "ECE20003",
    cname3 = "논리설계",
    cprof3 = "한윤식 교수님",

    ccode4 = "ECE20004",
    cname4 = "이산수학",
    cprof4 = "이건 교수님",

    ccode5 = "ECE20005",
    cname5 = "컴퓨터 구조",
    cprof5 = "용환기 교수님",

    ccode6 = "ECE20006",
    cname6 = "Data Structure",
    cprof6 = "이강 교수님",

    ccode7 = "ECE20007",
    cname7 = "공학설계입문",
    cprof7 = "한윤식 교수님",

    likenum1 = 120,
    likenum2 = 114,
    likenum3 = 106,
    likenum4 = 97,
    likenum5 = 95,
    likenum6 = 88,
    likenum7 = 82;

var eccode1 = document.getElementById('ccode1'),
    ecname1 = document.getElementById('cname1'),
    ecprof1 = document.getElementById('cprof1'),
             
    eccode2 = document.getElementById('ccode2'),
    ecname2 = document.getElementById('cname2'),
    ecprof2 = document.getElementById('cprof2'),

    eccode3 = document.getElementById('ccode3'),
    ecname3 = document.getElementById('cname3'),
    ecprof3 = document.getElementById('cprof3'),

    eccode4 = document.getElementById('ccode4'),
    ecname4 = document.getElementById('cname4'),
    ecprof4 = document.getElementById('cprof4'),

    eccode5 = document.getElementById('ccode5'),
    ecname5 = document.getElementById('cname5'),
    ecprof5 = document.getElementById('cprof5'),

    eccode6 = document.getElementById('ccode6'),
    ecname6 = document.getElementById('cname6'),
    ecprof6 = document.getElementById('cprof6'),

    eccode7 = document.getElementById('ccode7'),
    ecname7 = document.getElementById('cname7'),
    ecprof7 = document.getElementById('cprof7'),

    elikenum1 = document.getElementById('likenum1'),
    elikenum2 = document.getElementById('likenum2'),
    elikenum3 = document.getElementById('likenum3'),
    elikenum4 = document.getElementById('likenum4'),
    elikenum5 = document.getElementById('likenum5'),
    elikenum6 = document.getElementById('likenum6'),
    elikenum7 = document.getElementById('likenum7');

eccode1.textContent = ccode1;
ecname1.textContent = cname1;
ecprof1.textContent = cprof1;

eccode2.textContent = ccode2;
ecname2.textContent = cname2;
ecprof2.textContent = cprof2;

eccode3.textContent = ccode3;
ecname3.textContent = cname3;
ecprof3.textContent = cprof3;

eccode4.textContent = ccode4;
ecname4.textContent = cname4;
ecprof4.textContent = cprof4;

eccode5.textContent = ccode5;
ecname5.textContent = cname5;
ecprof5.textContent = cprof5;

eccode6.textContent = ccode6;
ecname6.textContent = cname6;
ecprof6.textContent = cprof6;

eccode7.textContent = ccode7;
ecname7.textContent = cname7;
ecprof7.textContent = cprof7;

elikenum1.textContent = likenum1;
elikenum2.textContent = likenum2;
elikenum3.textContent = likenum3;
elikenum4.textContent = likenum4;
elikenum5.textContent = likenum5;
elikenum6.textContent = likenum6;
elikenum7.textContent = likenum7;
});