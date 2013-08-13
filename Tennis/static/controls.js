$(document).ready(function(){
  // Autohides the placeholder whenever a textbox has content.
  $(".textboxWithPlaceholder").bind( "input", function(){
    var inputLength = $(this).val().length;
    if (inputLength > 0)
        $(this).css('background-color', 'white');
    else 
        $(this).css('background-color', 'transparent');
  });
  $.each($(".textboxWithPlaceholder"), function(){
    var inputLength = $(this).val().length;
    if (inputLength > 0)
        $(this).css('background-color', 'white');
    else 
        $(this).css('background-color', 'transparent');
  });
});
