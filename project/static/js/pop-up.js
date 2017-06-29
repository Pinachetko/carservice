$(function(){
    $(document).ready(function(){
     $(".pop-up-link").on("click", function(event)
     {
         event.preventDefault();
         $("div.pop-up-substrate").fadeIn(200);
         $("div.pop-up").fadeIn('slow');
         return false;
     });
    });
})
