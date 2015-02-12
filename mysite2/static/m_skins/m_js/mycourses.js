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

    sl01 = $('#sl111').slider(),
    sl02 = $('#sl112').slider(),
    sl03 = $('#sl113').slider(),
    sl04 = $('#sl114').slider(),
    sl05 = $('#sl121').slider(),
    sl06 = $('#sl122').slider(),
    sl07 = $('#sl123').slider(),
    sl08 = $('#sl124').slider(),
    sl09 = $('#sl131').slider(),
    sl010 = $('#sl132').slider(),
    sl011 = $('#sl133').slider(),
    sl012 = $('#sl134').slider(),
    sl013 = $('#sl141').slider(),
    sl014 = $('#sl142').slider(),
    sl015 = $('#sl143').slider(),
    sl016 = $('#sl144').slider(),
    sl017 = $('#sl151').slider(),
    sl018 = $('#sl152').slider(),
    sl019 = $('#sl153').slider(),
    sl020 = $('#sl154').slider(),
    sl021 = $('#sl161').slider(),
    sl022 = $('#sl162').slider(),
    sl023 = $('#sl163').slider(),
    sl024 = $('#sl164').slider();

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

$('#sl111').slider('disable');
$('#sl112').slider('disable');
$('#sl113').slider('disable');
$('#sl114').slider('disable');
$('#sl121').slider('disable');
$('#sl122').slider('disable');
$('#sl123').slider('disable');
$('#sl124').slider('disable');
$('#sl131').slider('disable');
$('#sl132').slider('disable');
$('#sl133').slider('disable');
$('#sl134').slider('disable');
$('#sl141').slider('disable');
$('#sl142').slider('disable');
$('#sl143').slider('disable');
$('#sl144').slider('disable');
$('#sl151').slider('disable');
$('#sl152').slider('disable');
$('#sl153').slider('disable');
$('#sl154').slider('disable');
$('#sl161').slider('disable');
$('#sl162').slider('disable');
$('#sl163').slider('disable');
$('#sl164').slider('disable');

$.get("../index.php", function(data){
    var datavalue = data.split(",");
    $('#sl11').slider('setValue', datavalue[0]);
    $('#sl12').slider('setValue', datavalue[1]);
    $('#sl13').slider('setValue', datavalue[2]);
    $('#sl14').slider('setValue', datavalue[3]);
});

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

$.get("../index.php", function(data){
    var datavalue = data.split(",");
    $('#sl111').slider('setValue', datavalue[0]);
    $('#sl112').slider('setValue', datavalue[1]);
    $('#sl113').slider('setValue', datavalue[2]);
    $('#sl114').slider('setValue', datavalue[3]);
});

$('#sl121').slider('setValue', 5);
$('#sl122').slider('setValue', 5);
$('#sl123').slider('setValue', 5);
$('#sl124').slider('setValue', 5);
$('#sl131').slider('setValue', 5);
$('#sl132').slider('setValue', 5);
$('#sl133').slider('setValue', 5);
$('#sl134').slider('setValue', 5);
$('#sl141').slider('setValue', 5);
$('#sl142').slider('setValue', 5);
$('#sl143').slider('setValue', 5);
$('#sl144').slider('setValue', 5);
$('#sl151').slider('setValue', 5);
$('#sl152').slider('setValue', 5);
$('#sl153').slider('setValue', 5);
$('#sl154').slider('setValue', 5);
$('#sl161').slider('setValue', 5);
$('#sl162').slider('setValue', 5);
$('#sl163').slider('setValue', 5);
$('#sl164').slider('setValue', 5);

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

    ccode11 = "ECE20018",
    cname11 = "C 프로그래밍",
    cprof11 = "최창범 교수님",

    ccode12 = "ECE20002",
    cname12 = "자바 프로그래밍",
    cprof12 = "김인중 교수님",

    ccode13 = "ECE20003",
    cname13 = "논리설계",
    cprof13 = "한윤식 교수님",

    ccode14 = "ECE20004",
    cname14 = "이산수학",
    cprof14 = "이건 교수님",

    ccode15 = "ECE20005",
    cname15 = "컴퓨터 구조",
    cprof15 = "용환기 교수님",

    ccode16 = "ECE20006",
    cname16 = "Data Structure",
    cprof16 = "이강 교수님",

    likenum1 = 120,
    likenum2 = 114,
    likenum3 = 106,
    likenum4 = 97,
    likenum5 = 95,
    likenum6 = 88,

    likenum11 = 120,
    likenum12 = 114,
    likenum13 = 106,
    likenum14 = 97,
    likenum15 = 95,
    likenum16 = 88;

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

    eccode11 = document.getElementById('ccode11'),
    ecname11 = document.getElementById('cname11'),
    ecprof11 = document.getElementById('cprof11'),
             
    eccode12 = document.getElementById('ccode12'),
    ecname12 = document.getElementById('cname12'),
    ecprof12 = document.getElementById('cprof12'),

    eccode13 = document.getElementById('ccode13'),
    ecname13 = document.getElementById('cname13'),
    ecprof13 = document.getElementById('cprof13'),

    eccode14 = document.getElementById('ccode14'),
    ecname14 = document.getElementById('cname14'),
    ecprof14 = document.getElementById('cprof14'),

    eccode15 = document.getElementById('ccode15'),
    ecname15 = document.getElementById('cname15'),
    ecprof15 = document.getElementById('cprof15'),

    eccode16 = document.getElementById('ccode16'),
    ecname16 = document.getElementById('cname16'),
    ecprof16 = document.getElementById('cprof16'),

    elikenum1 = document.getElementById('likenum1'),
    elikenum2 = document.getElementById('likenum2'),
    elikenum3 = document.getElementById('likenum3'),
    elikenum4 = document.getElementById('likenum4'),
    elikenum5 = document.getElementById('likenum5'),
    elikenum6 = document.getElementById('likenum6'),

    elikenum11 = document.getElementById('likenum11'),
    elikenum12 = document.getElementById('likenum12'),
    elikenum13 = document.getElementById('likenum13'),
    elikenum14 = document.getElementById('likenum14'),
    elikenum15 = document.getElementById('likenum15'),
    elikenum16 = document.getElementById('likenum16');

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

eccode11.textContent = ccode11;
ecname11.textContent = cname11;
ecprof11.textContent = cprof11;

eccode12.textContent = ccode12;
ecname12.textContent = cname12;
ecprof12.textContent = cprof12;

eccode13.textContent = ccode13;
ecname13.textContent = cname13;
ecprof13.textContent = cprof13;

eccode14.textContent = ccode14;
ecname14.textContent = cname14;
ecprof14.textContent = cprof14;

eccode15.textContent = ccode15;
ecname15.textContent = cname15;
ecprof15.textContent = cprof15;

eccode16.textContent = ccode16;
ecname16.textContent = cname16;
ecprof16.textContent = cprof16;

elikenum1.textContent = likenum1;
elikenum2.textContent = likenum2;
elikenum3.textContent = likenum3;
elikenum4.textContent = likenum4;
elikenum5.textContent = likenum5;
elikenum6.textContent = likenum6;

elikenum11.textContent = likenum11;
elikenum12.textContent = likenum12;
elikenum13.textContent = likenum13;
elikenum14.textContent = likenum14;
elikenum15.textContent = likenum15;
elikenum16.textContent = likenum16;
});