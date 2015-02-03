$(function(){

  $('#spanname').text('홍길동');  
  $('#spanyear').text('19500000');  
  $('#spannum1').text('도술학');  
  $('#spannum2').text('문학');  
  $('#spannum3').text('honggildongbest');  
  $('#spannum4').text('*******');  
  $('#spannum5').text('3');
  $('#spannum6').text('4');

  

  $('#btnnum4').click(function(){
      var txtbox1 = $('<input id="idtxtbox4" type="text">'),
          btn1 = $('<button id="changebtn4" class="btn btn-info">').text('Change'),
          btn2 = $('<button id="cancelbtn4" class="btn btn-info">').text('Cancel');

      $('#spannum4').hide();
      $('#spannum4').before(txtbox1);
      $('#idtxtbox4').val($('#spannum4').text());
      $('#btnnum4').hide();
      $('#btnnum4').before(btn1);
      $('#btnnum4').after(btn2);

  });

  $('div').on('click', '#cancelbtn4', function(){
      $('#idtxtbox4').remove();
      $('#changebtn4').remove();
      $('#cancelbtn4').remove();
      $('#spannum4').show();
      $('#btnnum4').show();
  });

  $('div').on('click', '#changebtn4', function(){
      var newpw = $('#idtxtbox4').val();

      if(newpw.length >= 6 && newpw.length <= 20){
        if( newpw.indexOf(" ") !== -1 ){
            alert("bad input");
        }
        else{
          if(/^[a-zA-Z0-9- ]*$/.test(newpw) == false) {
            alert('Your password contains illegal characters.');
          }
          else{
            var newpwhide = "";
            for(var i = 0; i < newpw.length; i++){
              newpwhide += "*";
            };
            alert('Successfully changed!');
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