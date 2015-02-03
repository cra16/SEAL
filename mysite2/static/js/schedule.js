$(document).ready(function () {
    
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