// Glass window

// by Mexalim
// - ICQ 590881221
// - Email info@mexalim.com.ua

(function($) {
  $(function() {
      var popwindow = $('.popwindow'); // РљР»Р°СЃСЃ РѕРєРЅР°
      var popbutton = $('.popbutton'); // РљР»Р°СЃСЃ РєРЅРѕРїРєРё
      $("body").prepend("<div class='mask'></div>");
      function preparewindow(windowobject) {
        var winwidth = windowobject.data("width");
        var winheight = windowobject.data("height");
        var winmargin = winwidth / 2;
        var wintitle = windowobject.data("title");

        windowobject.wrap("<div class='box_window'></div>");
        windowobject.addClass("box_window_in");
        windowobject.parent(".box_window").prepend("<div class='bw_close'>Р·Р°РєСЂС‹С‚СЊ</div>");
        windowobject.css("cursor","pointer");

        windowobject.parent(".box_window").prepend("<div class='box_title'>"+wintitle+"</div>");
        windowobject.parent(".box_window").css({'width':winwidth,'height':winheight,'margin-left':'-'+winmargin})
        windowobject.css({'height':winheight})
      }
      if (popwindow.length) {
        preparewindow(popwindow);
        popbutton.click(function(){
            var idwind = $(this).data("window");
            $("#" + idwind).parent(".box_window").fadeIn().addClass("windactiv");
            $(".mask").fadeIn();
            $(".to_blur").addClass("blur");
        });
      };
      $(".mask, .bw_close").click(function(){
          $(".windactiv").fadeOut();
          $(".windactiv").removeClass("windactiv");
          $(".mask").fadeOut();
           $(".to_blur").removeClass("blur");
      });
  });
})(jQuery)
