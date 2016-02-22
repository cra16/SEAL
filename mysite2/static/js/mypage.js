$(function(){

$('form').on('click', '#changebtn4',function(){
    
      var newnick = $('#Nickname').val();
     
      if(newnick.length >= 2 && newnick.length <= 10){
        if( newnick.indexOf(" ") !== -1 ){
            alert("잘못된 입력입니다");
        }
        else{
            //connect to DB at here
            $.ajax(
            { url : "/MyPage/NicknameChange/",
              data : {'Nickname' : $('#Nickname').val()},
              type : "POST",
              success:function(resp){  
                  alert('Successfully changed!');
                  } ,
              error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용
            }
              });
            
            $('#idtxtbox4').remove();
            $('#changebtn4').remove();
            $('#cancelbtn4').remove();

      $('#NickDiv').remove();
            $('#spannum4').show();
            $('#btnnum4').show();
          }
        }
      else {
        alert('닉네임은 2자 이상 10자 이하로 사용해야 합니다');
      }
  });
  $('#btnnum4').click(function(){
      var NicknameDiv = $(' <div id ="NickDiv" class="left floated left aligned nine wide column"><input type="text" id="Nickname"></div> ');
          
          btn1 = $('<button id="changebtn4" type = "button" class="btn btn-info">').text('Change');
          btn2 = $('<button id="cancelbtn4" type = "button" class="btn btn-info">').text('Cancel');

      $('#btnnum4').hide();
      $('#btnnum4').before(btn1);
      $('#btnnum4').after(btn2);
      $('#spannum4').hide();
        
      $('#NicknameChange').prepend(NicknameDiv);
    //  $('#PasswordD').show();
     

  });
 
  $('form').on('click', '#cancelbtn4', function(){
      $('#idtxtbox4').remove();
      $('#changebtn4').remove();
      $('#cancelbtn4').remove();
      $('#spannum4').show();
      $('#btnnum4').show();
  });

 

  $('#btnnum5').click(function(){
      window.location.href = "../html/mycourses.html";
  });

  $('#btnnum6').click(function(){
      window.location.href = "../html/mycourses.html";
  });

});
