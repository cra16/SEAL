$(document).ready(function()
{
	$('div').on('click',"#close",function(event){
         event.stopPropagation();
          $(this).unbind("click");
        var Find = $(this).parent().find("[id=open]");
        $(this).hide();
        $(Find).show();
    });
    $('div').on('click',"#open",function(event){
       event.stopPropagation();
          $(this).unbind("click");
        var Find = $(this).parent().find("[id=close]");
        

        $(this).hide();
        $(Find).show();
    });    
});