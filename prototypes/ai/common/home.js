$(function(){
  var includes = $('[data-include-html]');
  jQuery.each(includes, function(){
    var file = $(this).data('include-html');
    $(this).load(file);
  });
});
