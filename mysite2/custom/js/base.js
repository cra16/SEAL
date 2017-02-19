$(document).ready(function()
{
  $("div").on("click",".dropdown-toggle",function()
  {
    if($(".dropdown-toggle .dropdown-menu").css("display","block"))
      $(".dropdown-toggle .dropdown-menu").fadeIn("slow")
    else
      $(".dropdown-toggle .dropdown-menu").fadeOut("slow")
  })
	$('body').on('click','#category-subject',function(event)
  { 
      event.stopPropagation();
      
      $.ajax({
        url:"/Category_Search/",
        data :$("#category_subject_search").serialize(),
        datatype:"json",
        type:"GET",
        async:false,
        success:function(resp){     
                     $('#category_subject_search').next().remove();
                     $('#category_subject_search').next().remove();
                     $('#category_subject_search').after(resp);
                  },
                  error: function(xhr, option, error){
                    alert(xhr.status); //오류코드
                    alert(error); //오류내용

                  } 
      });
      return false;
  });
  $('body').on('click','.category_item',function(event)
  { 
      var data_value=$(this).attr("data-value");
   
      event.stopPropagation();
     
      var category_name = $(this).parent().parent().find('.text').eq(0).text();
      $.ajax({ 
              url : "/Category_Change/",
              data : {
                      'category_number':data_value,
                      'category_name':category_name
                    },
              
              datatype:"json",
              type : "GET",
              async : false,
              success:function(resp){     
                    $('.new_field').remove();
                    $('.field:first').after(resp);

                     $('.all_course').dropdown();
               
                     $('#category').val(data_value);

                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
          });

  });

  $('body').on('click','.detail_item',function(event)
  {
 
      event.stopPropagation();

      var category_name = $(this).parent().parent().find('.text').eq(0).text();
      $.ajax({ 
              url : "/Category_Subject_Change/",
              data:
                    {
                      'category_number':$('#category').val(),
                      'category_name':category_name
                    },
              
              datatype:"json",
              type : "GET",
              async : false,
              success:function(resp){     
                    $('.new_field').remove();
                    $('.field:first').after(resp);
                    $('.all_course').dropdown();
                    $('#major_category').val(category_name);
                    $('#major_category').prev().prev().text(category_name);
                },
                error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용

                  } 
            
        });
         
  });
  $('body').on('click','.subject_item',function(event)
  {  
    event.stopPropagation();
    var category_name = $(this).parent().parent().find('.text').eq(0).text();
    $('#major_category').val(category_name);
  });

  $('body').on('click','.category-search',function()
  {
     $.ajax({
            url : "/Search_Category_Subject/",
            data : {
                    'category_number':$('#category').val(),
                    'category_name':category_name
                  },
            
            datatype:"json",
            type : "GET",
            async : false,
            success:function(resp){     
                 
            },
            error: function(xhr, option, error){
                alert(xhr.status); //오류코드
                alert(error); //오류내용

                } 
          
      });

  });
  $('div').on('click',"#SubjectSearchPage",function(event)
  {
    event.stopPropagation();
    $(this).unbind("click");
    var CurrentPage=$(this).parent().attr("id")

    $.ajax({
          url : "/SubjectSearchPage/",
          data : {'Page': $(this).attr("name"),
                  'Current':CurrentPage,
                  'Course':$("#cname").text()
                },
          
          datatype:"json",
          type : "GET",
          async : false,
          success:function(resp){     
                 $('#Search_Page').html(resp);
           },
          error: function(xhr, option, error){
            alert(xhr.status); //ì˜¤ë¥˜ì½”ë“œ
            alert(error); //ì˜¤ë¥˜ë‚´ìš©

            } 
      
      
      });
  });

  $('div').on('click','#SubjectSearchNext',function()
  {
      event.stopPropagation();
      $(this).unbind("click");
      var CurrentPage=$(this).parent().attr("id")

      $.ajax({ 
            url : "/SubjectSearchPage/",
            data : {'Page': $(this).attr("name"),
                    'Current':CurrentPage,
                    'Course':$("#cname").text()
                    },
            
            datatype:"json",
            type : "GET",
            async : false,
            success:function(resp){     
                $('#Search_Page').html(resp);
              },
              error: function(xhr, option, error){
                alert(xhr.status); //ì˜¤ë¥˜ì½”ë“œ
                alert(error); //ì˜¤ë¥˜ë‚´ìš©

                } 
          
        });
  });

  $('div').on('click','#SubjectSearchPrevious',function()
  {
      event.stopPropagation();
      $(this).unbind("click");
      var CurrentPage=$(this).parent().attr("id")

      $.ajax({
            url : "/SubjectSearchPage/",
            data : {'Page': $(this).attr("name"),
                    'Current':CurrentPage,
                    'Course':$("#cname").text()
                  },
            
            datatype:"json",
            type : "GET",
            async : false,
            success:function(resp){     
                $('#Search_Page').html(resp);
              },
              error: function(xhr, option, error){
                alert(xhr.status); //ì˜¤ë¥˜ì½”ë“œ
                alert(error); //ì˜¤ë¥˜ë‚´ìš©

                } 
          
        });


  });
});