$(document).ready(function()
{
	$('div').on('click',"#close",function(event){
         event.stopPropagation();
          $(this).unbind("click");
        var Find = $(this).parent().find("[id=open]");
        alert("GG");
        $(this).hide();
        $(Find).show();
    });
    $('div').on('click',"#open",function(event){
       event.stopPropagation();
          $(this).unbind("click");
        var Find = $(this).parent().find("[id=close]");
        
        alert("FF");
        $(this).hide();
        $(Find).show();
    });    
});