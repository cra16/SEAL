$(function(){


  $('#selectnum1').hide();
  $('#selectnum2').hide();

  $('#btnnum1').click(function(){
      var btn1 = $('<button id="changebtn1" class="btn btn-info">').text('Change'),
          btn2 = $('<button id="cancelbtn1" class="btn btn-info">').text('Cancel');

      $('#spannum1').hide();
      $('#selectnum1').show();
      $('#btnnum1').hide();
      $('#btnnum1').before(btn1);
      $('#btnnum1').after(btn2);

  });

  $('div').on('click', '#cancelbtn1', function(){
      $('#selectnum1').hide();
      $('#changebtn1').remove();
      $('#cancelbtn1').remove();
      $('#spannum1').show();
      $('#btnnum1').show();
  });

  $('div').on('click', '#changebtn1', function(){
      var selected = $("#selectnum1 option:selected").text();
      $('#spannum1').text(selected);
      $('#selectnum1').hide();
      $('#changebtn1').remove();
      $('#cancelbtn1').remove();
      $('#spannum1').show();
      $('#btnnum1').show();
      alert('Successfully changed!');
  });

  $('#btnnum2').click(function(){
      var btn1 = $('<button id="changebtn2" class="btn btn-info">').text('Change'),
          btn2 = $('<button id="cancelbtn2" class="btn btn-info">').text('Cancel');

      $('#spannum2').hide();
      $('#selectnum2').show();
      $('#btnnum2').hide();
      $('#btnnum2').before(btn1);
      $('#btnnum2').after(btn2);

  });

  $('div').on('click', '#cancelbtn2', function(){
      $('#selectnum2').hide();
      $('#changebtn2').remove();
      $('#cancelbtn2').remove();
      $('#spannum2').show();
      $('#btnnum2').show();
  });

  $('div').on('click', '#changebtn2', function(){
      var selected = $("#selectnum2 option:selected").text();
      $('#spannum2').text(selected);
      $('#selectnum2').hide();
      $('#changebtn2').remove();
      $('#cancelbtn2').remove();
      $('#spannum2').show();
      $('#btnnum2').show();
      alert('Successfully changed!');
  });

  $('#btnnum3').click(function(){
      var txtbox1 = $('<input id="idtxtbox3" type="text">'),
          btn1 = $('<button id="changebtn3" class="btn btn-info">').text('Change'),
          btn2 = $('<button id="cancelbtn3" class="btn btn-info">').text('Cancel');

      $('#spannum3').hide();
      $('#spannum3').before(txtbox1);
      $('#idtxtbox3').val($('#spannum3').text());
      $('#btnnum3').hide();
      $('#btnnum3').before(btn1);
      $('#btnnum3').after(btn2);

  });

  $('div').on('click', '#cancelbtn3', function(){
      $('#idtxtbox3').remove();
      $('#changebtn3').remove();
      $('#cancelbtn3').remove();
      $('#spannum3').show();
      $('#btnnum3').show();
  });

  $('div').on('click', '#changebtn3', function(){
      var newid = $('#idtxtbox3').val();

      if(newid.length >= 6 && newid.length <= 20){

        if( newid.indexOf(" ") !== -1 ){
            alert("bad input");
	  }
	  else{
          if(/^[a-zA-Z0-9- ]*$/.test(newid) == false) {
            alert('Your password contains illegal characters.');
          }
          else{
            alert('Successfully changed!');
            $('#spannum3').text(newid);
            $('#idtxtbox3').remove();
            $('#changebtn3').remove();
            $('#cancelbtn3').remove();
            $('#spannum3').show();
            $('#btnnum3').show();
          }
        }
      }
      else {
        alert('ID는 6자 이상, 20자 이하여야합니다.');
      }
  });

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
