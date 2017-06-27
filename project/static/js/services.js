$(function() {
    var Accordion = function(el, multiple) {
        this.el = el || {};
        this.multiple = multiple || false;
        var links = this.el.find('.link');
        links.on('click', {el: this.el, multiple: this.multiple}, this.dropdown)
    }

    Accordion.prototype.dropdown = function(e) {
        var $el = e.data.el;
        $this = $(this),
        $next = $this.next();
        $next.slideToggle();
        $this.parent().toggleClass('open');

        if (!e.data.multiple) {
            $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
        };
    }

    var accordion = new Accordion($('#menu'), false);
});

function ajaxPagination(page_number, event){
    var page_number = page_number;
    var data = {};
    var url =$(event.target).attr("post-url");
    if(!$.browser.mozilla){
      event.preventDefault();
  }
  $.ajax({
      beforeSend: function () {
        showPreloader();
    },
    url: url,
    type: "POST",
    data: data,
    cache: false,
    success: function(data){
        if (data.html != ''){
          $("table#price-list tbody").empty().html(data["html"]);
          hidePreloader();
      }
  }
})
}

function showPreloader(){
    $("div.spinner").addClass("loader08");
    $(".content-wrapper").attr("id","page-preloader");
}

function hidePreloader(){
    $(".content-wrapper").attr("id","");
    $("div.spinner").removeClass("loader08");
    var destination = $("h3#price-list-header").offset().top;
    $('body').animate( { scrollTop: destination -40 }, 1100 );
}

$(function(){
    $("a.link-car-filter").on("click", function(event){
      var data = {};
      var url = $(event.target).attr("post-url");
      history.pushState(null, null, url);
      var currentCaregory = $(event.target).parents(".menu-lvl-1").children("div.link").text();
      $("div.page-header-left h1").text(currentCaregory.toUpperCase());
      $("a#current-dir").text(currentCaregory.toUpperCase()).attr("href", url);
      $.ajax({
        beforeSend: function () {
          showPreloader();
      },
      url: url,
      type: "POST",
      data: data,
      cache: false,
      success: function(data){
          if (data.html != ''){
            $("li.menu-lvl-1").removeClass("selected");
            $("li.menu-lvl-2.selected").removeClass("selected");
            $(event.target).parents(".menu-lvl-1").addClass("selected");
            $(event.target).parent().addClass("selected");
            $("table#price-list tbody").empty().html(data["html"]);
            $("#light-pagination").pagination({
              pages: data["count_pages"],
              displayedPages: 7,
              currentPage : data["current_page"],
              hrefTextPrefix: data["hrefTextPrefix"],
              hrefTextSuffix: "/",
              prevText : "<<",
              nextText: ">>",
              cssStyle: 'light-theme',
              selectOnClick: true,
              onPageClick: ajaxPagination,
          });
            hidePreloader();
        }
    }
})
  })
})
