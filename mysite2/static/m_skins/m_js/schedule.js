$(document).ready(function () {

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

          likenum1 = 120,
          likenum2 = 114,
          likenum3 = 106,
          likenum4 = 97,
          likenum5 = 95,
          likenum6 = 88,
                
          cperiod1 = "월5 목5",
          cperiod2 = "월5 목5",
          cperiod3 = "목5 목6",
          cperiod4 = "월5 목5",
          cperiod5 = "월5 목5",
          cperiod6 = "목4 목5";

                
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

          elikenum1 = document.getElementById('likenum1'),
          elikenum2 = document.getElementById('likenum2'),
          elikenum3 = document.getElementById('likenum3'),
          elikenum4 = document.getElementById('likenum4'),
          elikenum5 = document.getElementById('likenum5'),
          elikenum6 = document.getElementById('likenum6'),

          ecperiod1 = document.getElementById('cperiod1'),
          ecperiod2 = document.getElementById('cperiod2'),
          ecperiod3 = document.getElementById('cperiod3'),
          ecperiod4 = document.getElementById('cperiod4'),
          ecperiod5 = document.getElementById('cperiod5'),
          ecperiod6 = document.getElementById('cperiod6');
          
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

      elikenum1.textContent = likenum1;
      elikenum2.textContent = likenum2;
      elikenum3.textContent = likenum3;
      elikenum4.textContent = likenum4;
      elikenum5.textContent = likenum5;
      elikenum6.textContent = likenum6;

      ecperiod1.textContent = cperiod1;
      ecperiod2.textContent = cperiod2;
      ecperiod3.textContent = cperiod3;
      ecperiod4.textContent = cperiod4;
      ecperiod5.textContent = cperiod5;
      ecperiod6.textContent = cperiod6;
    
    
    $('#sch-result').hide();
    
    $('.table td').css( 'cursor', 'pointer' );
    
    var arr=['월요일', '화요일', '수요일', '목요일', '금요일', '토요일'];
    
    $('.table td').click(function(event) {
    if(confirm((arr[$(this).index()-1]) + " " + ($(this).parent().index()+1) + "교시 수업을 검색하시겠습니까?")==true)
    {$('#sch-result').fadeIn();};
    });
    
    $('#sch-search').click(function(event) {
        $('#sch-result').fadeIn();
    });
    
    $('#sch-result .button').click(function(event) {
        $('#sch-result').fadeOut(100);
    });
		    
});