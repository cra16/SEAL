$(function(){
  $("#NicknameChange").submit(function(e){
    return false;
  });
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
                  location.reload();
                  } ,
              error: function(xhr, option, error){
                  alert('중복되는 닉네임이 존재합니다'); //오류내용
            }
              });
            
          }
        }
      else {
        alert('닉네임은 2자 이상 10자 이하로 사용해야 합니다');
      }
  });
  $("#Nickname").keydown(function (key) {
    if (key.keyCode == 13) {
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
                  location.reload();
                  } ,
              error: function(xhr, option, error){
                  alert('중복되는 닉네임이 존재합니다'); //오류내용
            }
              });
            
          }
        }
      else {
        alert('닉네임은 2자 이상 10자 이하로 사용해야 합니다');
      }
    }
  });


  $('#btnnum4').click(function(){
      var NicknameDiv = $(' <div id ="NickDiv" class="left floated left aligned nine wide column"><input type="text" id="Nickname"></div> ');
          
          btn1 = $('<button id="changebtn4" type = "button" class="btn btn-info">').text('Change');
          btn2 = $('<button id="cancelbtn4" type = "button" class="btn btn-info">').text('Cancel');

      $('#thirdcolumn').hide();
      $('#btnnum4').hide();
      $('#btnnum4').before(btn1);
      $('#btnnum4').after(btn2);
      $('#spannum4').hide();
        
      $('#NicknameChange').prepend(NicknameDiv);
    //  $('#PasswordD').show();
     

  });
 
  $('form').on('click', '#cancelbtn4', function(){
      $('#Nickname').remove();
      $('#changebtn4').remove();
      $('#cancelbtn4').remove();
      $('#spannum4').show();
      $('#btnnum4').show();
      $('#thirdcolumn').show();
  });

 

  $('#btnnum5').click(function(){
      window.location.href = "../html/mycourses.html";
  });

  $('#btnnum6').click(function(){
      window.location.href = "../html/mycourses.html";
  });

});
