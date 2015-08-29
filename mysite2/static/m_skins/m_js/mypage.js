$(function(){

$('form').on('click', '#changebtn4',function(){
    
      var newpw = $('#PasswordBox').val();
     
      if(newpw.length >= 6 && newpw.length <= 20){
        if( newpw.indexOf(" ") !== -1 ){
            alert("bad input");
        }
        else{
          if(/^[a-zA-Z0-9- ]*$/.test(newpw) == false) {
            alert('Your password contains illegal characters.');
          }
          else{   
            //connect to DB at here
            var newpwhide = "";
            for(var i = 0; i < newpw.length; i++){
              newpwhide += "*";
            }
           
            $.ajax(
            { url : "/MyPage/PasswordChange/",
              data : {'PasswordBox' : $('#PasswordBox').val()},
              type : "POST",
              success:function(resp){  
                  alert('Successfully changed!');
                  } ,
              error: function(xhr, option, error){
                  alert(xhr.status); //오류코드
                  alert(error); //오류내용
            }
              });
            
            $('#spannum4').text(newpwhide);
            $('#idtxtbox4').remove();
            $('#changebtn4').remove();
            $('#cancelbtn4').remove();

      $('#PasswordD').remove();
            $('#spannum4').show();
            $('#btnnum4').show();
          }
        }
      }
      else {
        alert('비밀번호는 6자 이상, 20자 이하여야합니다.');
      }
  });
  $('#btnnum4').click(function(){
      var PasswordDiv = $(' <div id ="PasswordD" class="left floated left aligned nine wide column"><span id = "firstcolumn"> 비밀번호 :</span> <input type="password" id="PasswordBox"> <span id="PasswordData"></span><span id = "secondcolumn"> 비밀번호 확인 :</span> <input type="password" id="RePasswordBox"> </div> ');
          
          btn1 = $('<button id="changebtn4" type = "button" class="btn btn-info">').text('Change'),
          btn2 = $('<button id="cancelbtn4" type = "button" class="btn btn-info">').text('Cancel');

      $('#btnnum4').hide();
      $('#btnnum4').before(btn1);
      $('#btnnum4').after(btn2);
      $('#spannum4').hide();
        
      $('#PasswordChange').prepend(PasswordDiv);
    //  $('#PasswordD').show();
     

  });
 
  $('form').on('click', '#cancelbtn4', function(){
      $('#idtxtbox4').remove();
      $('#changebtn4').remove();
      $('#cancelbtn4').remove();
      $('#PasswordBox').remove();
      $('#RePasswordBox').remove();
      $('#PassWordText').remove();
      $('#RePassWordText').remove();
      $('#PasswordD').remove();
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
