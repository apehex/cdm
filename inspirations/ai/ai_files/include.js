$(function(){
  var includes = $('[data-include-html]');
  jQuery.each(includes, function(){
    var file = $(this).data('include-html');
    $.get(file)
    .done(function() { 
        console.log('sex');
    }).fail(function() { 
        console.log('loose');
    })
    $(this).load(file);
  });
});
