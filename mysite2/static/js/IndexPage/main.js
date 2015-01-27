$(document).ready(function() {
    
    $('.message .glyphicon').on('click', function() {
      $(this).closest('.message').fadeOut();
    });
    
});