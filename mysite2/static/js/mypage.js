$(function(){

  $('#btnnum4').click(function(){
      var PassWordText = $('<span id = "firstcolumn"> 비밀번호 :</span> '),
          RePassWordText =('<span id = "secondcolumn"> 비밀번호 확인 :</span> '),
          txtbox1 = $('<input type="password" id="PasswordBox">'),
          txtbox2 = $('<input type="password" id="RePasswordBox">'),
          btn1 = $('<button id="changebtn4" type = "button" class="btn btn-info">').text('Change'),
          btn2 = $('<button id="cancelbtn4" type = "button" class="btn btn-info">').text('Cancel');

      

      $('#btnnum4').hide();
      $('#btnnum4').before(btn1);
      $('#btnnum4').after(btn2);
      $('#spannum4').hide();
      $('#PasswordData').before(PassWordText);
      $('#PasswordData').after(txtbox1);
      $('#PasswordBox').after(txtbox2); 
      $('#PasswordBox').after(RePassWordText);
 

  });

  $('div').on('click', '#cancelbtn4', function(){
      $('#idtxtbox4').remove();
      $('#changebtn4').remove();
      $('#cancelbtn4').remove();
      $('#PasswordBox').remove();
      $('#RePasswordBox').remove();
      $('#firstcolumn').hide();
      $('#second  column').hide();
      
      $('#spannum4').show();
      $('#btnnum4').show();
  });

  $('div').on('click', '#changebtn4', function(){
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
            };
           
            $.ajax(
            { url : "/mysite2/MyPage/PasswordChange",
              data : {'PasswordBox' : $('#PasswordBox').val()},
              type : "POST",
              success:function(resp){  
                  alert('Successfully changed!');
                  } 
            }
              );
            
            $('#spannum4').text(newpwhide);
            $('#idtxtbox4').remove();
            $('#changebtn4').remove();
            $('#cancelbtn4').remove();
            $('#spannum4').show();
            $('#btnnum4').show();
          }
        }
      }
      else {
        alert('비밀번호는 6자 이상, 20자 이하여야합니다.');
      }
  });

  $('#btnnum5').click(function(){
      window.location.href = "../html/mycourses.html";
  });

  $('#btnnum6').click(function(){
      window.location.href = "../html/mycourses.html";
  });

});
