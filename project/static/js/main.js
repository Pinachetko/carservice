"use strict";
window.odometerOptions = {
  auto: true, // Don't automatically initialize everything with class 'odometer'
  selector: '.number.animated-element', // Change the selector used to automatically find things to be animated
  format: '(ddd).dd', // Change how digit groups are formatted, and how many digits are shown after the decimal point
  duration: 1000, // Change how long the javascript expects the CSS animation to take
  theme: 'default', // Specify the theme (if you have more than one theme css file on the page)
  animation: 'count' // Count is a simpler animation method which just increments the value,
                     // use it when you're looking for something more subtle.
};
var map = null;
var marker = null;
var menu_position = null;

jQuery(document).ready(function($){
	//search form
	$(".search-container .template-search").on("click", function(event){
		event.preventDefault();
		$(this).parent().children(".search").toggle();
	});
	//mobile menu
	$(".mobile-menu-switch").on("click", function(event){
		event.preventDefault();
		if(!$(".mobile-menu").is(":visible"))
			$(".mobile-menu-divider").css("display", "block");
		$(".mobile-menu").slideToggle(500, function(){
			if(!$(".mobile-menu").is(":visible"))
				$(".mobile-menu-divider").css("display", "none");
		});
	});
	$(".collapsible-mobile-submenus .template-arrow-menu").on("click", function(event){
		event.preventDefault();
		$(this).next().slideToggle(300);
	});
	//header toggle
	$(".header-toggle").on("click", function(event){
		event.preventDefault();
		$(this).prev().slideToggle();
		$(this).toggleClass("active");
	});
	//cost calculator
	$(".cost-slider").each(function(){
		$(this).slider({
			range: "min",
			value: $(this).data("value"),
			min: $(this).data("min"),
			max: $(this).data("max"),
			step: $(this).data("step"),
			slide: function(event, ui){
				$("#" + $(this).data("input")).val(ui.value);
				$(this).find(".cost-slider-tooltip .value").html(ui.value);
				if(typeof($(this).data("price"))!="undefined")
					$("#" + $(this).data("value-input")).val(ui.value*$(this).data("price"));
				$("#interior-renovation-cost").costCalculator("calculate");
				$("#fence-cost").costCalculator("calculate");
				$("#paver-walkway-cost").costCalculator("calculate");
			},
			change: function(event, ui){
				$("#" + $(this).data("input")).val(ui.value);
				$(this).find(".cost-slider-tooltip .value").html(ui.value);
				if(typeof($(this).data("price"))!="undefined")
					$("#" + $(this).data("value-input")).val(ui.value*$(this).data("price"));
				$("#interior-renovation-cost").costCalculator("calculate");
				$("#fence-cost").costCalculator("calculate");
				$("#paver-walkway-cost").costCalculator("calculate");
			}
		}).find(".ui-slider-handle").append('<div class="cost-slider-tooltip"><div class="arrow"></div><div class="value">' + $(this).data("value") + '</div></div>');
	});
	$(".cost-slider-input").on("paste change keyup", function(){
		var self = $(this);
		if(self.attr("type")=="checkbox")
		{
			if(self.is(":checked"))
				self.val(self.data("value"));
			else
				self.val(0);
		}
		if($("[data-input='" + self.attr("id") + "']").length)
			setTimeout(function(){
				$("[data-input='" + self.attr("id") + "']").slider("value", self.val());
			}, 500);
		else
		{
			$("#interior-renovation-cost").costCalculator("calculate");
			$("#fence-cost").costCalculator("calculate");
			$("#paver-walkway-cost").costCalculator("calculate");
		}
	});
	$(".cost-dropdown").each(function(){
		$(this).selectmenu({
			/*width: 370,*/
			icons: { button: "template-arrow-dropdown" },
			change: function(event, ui){
				$("#interior-renovation-cost").costCalculator("calculate");
				$("#fence-cost").costCalculator("calculate");
				$("#paver-walkway-cost").costCalculator("calculate");
				$("." + $(this).attr("id")).val(ui.item.label);
			},
			select: function(event, ui){
				$("#interior-renovation-cost").costCalculator("calculate");
				$("#fence-cost").costCalculator("calculate");
				$("#paver-walkway-cost").costCalculator("calculate");
				$("." + $(this).attr("id")).val(ui.item.label);
			},
			create: function(event, ui){
				$(".contact-form").each(function(){
					$(this)[0].reset();
				});
				$(this).selectmenu("refresh")
			}
		});
	});
	/*$.datepicker.regional['nl'] = {clearText: 'Effacer', clearStatus: '',
		closeText: 'sluiten', closeStatus: 'Onveranderd sluiten ',
		prevText: '<vorige', prevStatus: 'Zie de vorige maand',
		nextText: 'volgende>', nextStatus: 'Zie de volgende maand',
		currentText: 'Huidige', currentStatus: 'Bekijk de huidige maand',
		monthNames: ['januari','februari','maart','april','mei','juni',
		'juli','augustus','september','oktober','november','december'],
		monthNamesShort: ['jan','feb','mrt','apr','mei','jun',
		'jul','aug','sep','okt','nov','dec'],
		monthStatus: 'Bekijk een andere maand', yearStatus: 'Bekijk nog een jaar',
		weekHeader: 'Sm', weekStatus: '',
		dayNames: ['zondag','maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag'],
		dayNamesShort: ['zo', 'ma','di','wo','do','vr','za'],
		dayNamesMin: ['zo', 'ma','di','wo','do','vr','za'],
		dayStatus: 'Gebruik DD als de eerste dag van de week', dateStatus: 'Kies DD, MM d',
		dateFormat: 'dd/mm/yy', firstDay: 1,
		initStatus: 'Kies een datum', isRTL: false};
	$.datepicker.setDefaults($.datepicker.regional['nl']);*/
	$(".cost-slider-datepicker").each(function(){
		$(this).datepicker({
			dateFormat: "DD, d MM yy",
			nextText: "",
			prevText: ""
		});
	});
	$(".datepicker-container .ui-icon").on("click", function(){
		$(this).next().datepicker("show");
	});
	$("#interior-renovation-cost").costCalculator({
		formula: "ir-square-feet*ir-walls+ir-square-feet*ir-floors+ir-doors-value+ir-windows-value",
		currency: "$",
		updateHidden: $("#ir-total-cost")
	});
	$("#fence-cost").costCalculator({
		formula: "fe-length*fe-height*fe-panel+fe-gate+fe-length*fe-extras",
		currency: "$",
		updateHidden: $("#fe-total-cost")
	});
	$("#paver-walkway-cost").costCalculator({
		formula: "pw-area-width*pw-area-length*pw-block-paving+pw-area-width*pw-area-length*pw-surface+pw-stone-walling-value",
		currency: "$",
		updateHidden: $("#pw-total-cost")
	});

	//slider
	jQuery('.revolution-slider').show().revolution({
		dottedOverlay:"none",
		delay:10000,
		gridwidth:1170,
		gridheight:600,
		sliderLayout:"auto",
		navigation: {
			keyboardNavigation:"on",
			onHoverStop:"on",
			touch:{
				touchenabled:"on",
				swipe_treshold : 75,
				swipe_min_touches : 1,
				drag_block_vertical:false,
				swipe_direction:"horizontal"
            },
			arrows: {
				style:"preview1",
				enable:true,
				hide_onmobile:true,
				hide_onleave:true,
				hide_delay:200,
				hide_delay_mobile:1500,
				hide_under:0,
				hide_over:9999,
				tmp:'',
				left : {
					h_align:"left",
					v_align:"center",
					h_offset:0,
					v_offset:0,
				},
				right : {
					h_align:"right",
					v_align:"center",
					h_offset:0,
					v_offset:0
				}
			},
			bullets: {
				style:"preview1",
				enable:true,
				hide_onmobile:true,
				hide_onleave:true,
				hide_delay:200,
				hide_delay_mobile:1500,
				hide_under:0,
				hide_over:9999,
				direction:"horizontal",
				h_align:"center",
				v_align:"bottom",
				space:10,
				h_offset:0,
				v_offset:20,
				tmp:'<span class="tp-bullet-image"></span><span class="tp-bullet-title"></span>'
			},
			parallax:{
			   type:"off",
			   bgparallax:"off",
			   disable_onmobile:"on"
			}
		},
		shadow:0,
		spinner:"spinner0",
		stopAfterLoops:-1,
		stopAtSlide:-1,
		disableProgressBar: "on"
	});

	//parallax
	if(!navigator.userAgent.match(/(iPod|iPhone|iPad|Android)/))
		$(".parallax").parallax({
			speed: 100,
			startPosition: 0/*,
			startPosition: -1500*/
		});
	else
		$(".parallax").addClass("cover");

	//isotope
	$(".isotope").isotope({
		masonry: {
			//columnWidth: 225,
			gutter: 30
		}
	});

	//testimonials
	$(".testimonials-list").each(function(){
		var self = $(this);
		self.carouFredSel({
			/*responsive: true,*/
			width: "auto",
			items: {
				visible: 1
			},
			scroll: {
				items: 1,
				easing: "easeInOutQuint",
				duration: 750
			},
			auto: {
				play: false
			},
			'prev': {button: self.prev()},
			'next': {button: self.next()}
		},
		{
			transition: true,
			wrapper: {
				classname: "caroufredsel_wrapper caroufredsel_wrapper_testimonials"
			}
		});
		var base = "x";
		var scrollOptions = {
			scroll: {
				easing: "easeInOutQuint",
				duration: 750
			}
		};
		self.swipe({
			fallbackToMouseEvents: true,
			allowPageScroll: "vertical",
			excludedElements:"button, input, select, textarea, .noSwipe",
			swipeStatus: function(event, phase, direction, distance, fingerCount, fingerData ) {
				//if(!self.is(":animated") && (!$(".control-for-" + self.attr("id")).length || ($(".control-for-" + self.attr("id")).length && !$(".control-for-" + self.attr("id")).is(":animated"))))
				if(!self.is(":animated"))
				{
					self.trigger("isScrolling", function(isScrolling){
						if(!isScrolling)
						{
							if (phase == "move" && (direction == "left" || direction == "right"))
							{
								if(base=="x")
								{
									self.trigger("configuration", scrollOptions);
									self.trigger("pause");
								}
								if (direction == "left")
								{
									if(base=="x")
										base = 0;
									self.css("left", parseInt(base, 10)-distance + "px");
								}
								else if (direction == "right")
								{
									if(base=="x" || base==0)
									{
										self.children().last().prependTo(self);
										base = -self.children().first().width();
									}
									self.css("left", base+distance + "px");
								}

							}
							else if (phase == "cancel")
							{
								if(distance!=0)
								{
									self.trigger("play");
									self.animate({
										"left": base + "px"
									}, 750, "easeInOutQuint", function(){
										if(base==-self.children().first().width())
										{
											self.children().first().appendTo(self);
											self.css("left", "0px");
											base = "x";
										}
										self.trigger("configuration", {scroll: {
											easing: "easeInOutQuint",
											duration: 750
										}});
									});
								}
							}
							else if (phase == "end")
							{
								self.trigger("play");
								if (direction == "right")
								{
									self.animate({
										"left": 0 + "px"
									}, 750, "easeInOutQuint", function(){
										self.trigger("configuration", {scroll: {
											easing: "easeInOutQuint",
											duration: 750
										}});
										base = "x";
									});
								}
								else if (direction == "left")
								{
									if(base==-self.children().first().width())
									{
										self.children().first().appendTo(self);
										self.css("left", (parseInt(self.css("left"), 10)-base)+"px");
									}
									self.trigger("nextPage");
									base = "x";
								}
							}
						}
					});
				}
			}
		});
	});
	//our-clients
	$(".our-clients-list").each(function(index){
		$(this).addClass("re-preloader_" + index);
		$(".re-preloader_" + index).before("<span class='re-preloader'></span>");
		$(".re-preloader_" + index + " img:first").one("load", function(){
			$(".re-preloader_" + index).prev(".re-preloader").remove();
			$(".re-preloader_" + index).fadeTo("slow", 1, function(){
				$(this).css("opacity", "");
			});
			var self = $(".re-preloader_" + index);
			self.carouFredSel({
				items: {
					visible: ($(".header").width()>750 ? 6 : ($(".header").width()>462 ? 4 : 2))
				},
				scroll: {
					items: ($(".header").width()>750 ? 6 : ($(".header").width()>462 ? 4 : 2)),
					easing: "easeInOutQuint",
					duration: 750
				},
				auto: {
					play: false
				},
				pagination: {
					items: ($(".header").width()>750 ? 6 : ($(".header").width()>462 ? 4 : 2)),
					container: $(self).next()
				}
			});
			var base = "x";
			var scrollOptions = {
				scroll: {
					easing: "easeInOutQuint",
					duration: 750
				}
			};
			self.swipe({
				fallbackToMouseEvents: true,
				allowPageScroll: "vertical",
				excludedElements:"button, input, select, textarea, .noSwipe",
				swipeStatus: function(event, phase, direction, distance, fingerCount, fingerData ) {
					//if(!self.is(":animated") && (!$(".control-for-" + self.attr("id")).length || ($(".control-for-" + self.attr("id")).length && !$(".control-for-" + self.attr("id")).is(":animated"))))
					if(!self.is(":animated"))
					{
						self.trigger("isScrolling", function(isScrolling){
							if(!isScrolling)
							{
								if (phase == "move" && (direction == "left" || direction == "right"))
								{
									if(base=="x")
									{
										self.trigger("configuration", scrollOptions);
										self.trigger("pause");
									}
									if (direction == "left")
									{
										if(base=="x")
											base = 0;
										self.css("left", parseInt(base, 10)-distance + "px");
									}
									else if (direction == "right")
									{
										if(base=="x" || base==0)
										{
											self.children().last().prependTo(self);
											base = -self.children().first().width()-parseInt(self.children().first().css("margin-right"), 10);
										}
										self.css("left", base+distance + "px");
									}

								}
								else if (phase == "cancel")
								{
									if(distance!=0)
									{
										self.trigger("play");
										self.animate({
											"left": base + "px"
										}, 750, "easeInOutQuint", function(){
											if(base==-self.children().first().width()-parseInt(self.children().first().css("margin-right"), 10))
											{
												self.children().first().appendTo(self);
												self.css("left", "0px");
												base = "x";
											}
											self.trigger("configuration", {scroll: {
												easing: "easeInOutQuint",
												duration: 750
											}});
										});
									}
								}
								else if (phase == "end")
								{
									self.trigger("play");
									if (direction == "right")
									{
										self.trigger("prevPage");
										self.children().first().appendTo(self);
										self.animate({
											"left": 0 + "px"
										}, 200, "linear", function(){
											self.trigger("configuration", {scroll: {
												easing: "easeInOutQuint",
												duration: 750
											}});
											base = "x";
										});
									}
									else if (direction == "left")
									{
										if(base==-self.children().first().width()-parseInt(self.children().first().css("margin-right"), 10))
										{
											self.children().first().appendTo(self);
											self.css("left", (parseInt(self.css("left"), 10)-base)+"px");
										}
										self.trigger("nextPage");
										self.trigger("configuration", {scroll: {
											easing: "easeInOutQuint",
											duration: 750
										}});
										base = "x";
									}
								}
							}
						});
					}
				}
			});
		}).each(function(){
			if(this.complete)
				$(this).load();
		});
	});

	//accordion
	$(".accordion").accordion({
		event: 'change',
		heightStyle: 'content',
		icons: {"header": "template-arrow-circle-right", "activeHeader": "template-arrow-circle-down"},
		/*active: false,
		collapsible: true*/
		create: function(event, ui){
			$(window).trigger('resize');
			$(".horizontal_carousel").trigger('configuration', ['debug', false, true]);
		}
	});
	$(".accordion.wide").on("accordionchange", function(event, ui){
		$("html, body").animate({scrollTop: $("#"+$(ui.newHeader).attr("id")).offset().top}, 400);
	});
	$(".tabs:not('.no-scroll')").on("tabsbeforeactivate", function(event, ui){
		$("html, body").animate({scrollTop: $("#"+$(ui.newTab).children("a").attr("id")).offset().top}, 400);
	});
	$(".tabs").tabs({
		event: 'change',
		show: true,
		create: function(){
			$("html, body").scrollTop(0);
		},
		activate: function(event, ui){
			ui.oldPanel.find(".submit-contact-form, [name='submit'], [name='name'], [name='email'], [name='message']").qtip('hide');
		}
	});

	//browser history
	$(".tabs .ui-tabs-nav a").on("click", function(){
		if($(this).attr("href").substr(0,4)!="http")
			$.bbq.pushState($(this).attr("href"));
		else
			window.location.href = $(this).attr("href");
	});
	$(".ui-accordion .ui-accordion-header").on("click", function(){
		$.bbq.pushState("#" + $(this).attr("id").replace("accordion-", ""));
	});

	//preloader
	var preloader = function()
	{
		$(".blog a.post-image>img, .post.single .post-image img, .services-list a>img, .galleries-list:not('.isotope') a>img, .re-preload>img").each(function(){
			$(this).before("<span class='re-preloader'></span>");
			$(this).one("load", function(){
				$(this).prev(".re-preloader").remove();
				$(this).fadeTo("slow", 1, function(){
					$(this).css("opacity", "");
				});
				$(this).css("display", "block");
			}).each(function(){
				if(this.complete || $(this).height()>0)
					$(this).load();
			});
		});

	};
	preloader();

	$(".scroll-to-comments").on("click", function(event){
		event.preventDefault();
		var offset = $("#comments-list").offset();
		if(typeof(offset)!="undefined")
			$("html, body").animate({scrollTop: offset.top-90}, 400);
	});
	$(".scroll-to-comment-form").on("click", function(event){
		event.preventDefault();
		var offset = $("#comment-form").offset();
		if(typeof(offset)!="undefined")
			$("html, body").animate({scrollTop: offset.top-90}, 400);
	});
	//hashchange
	$(window).on("hashchange", function(event){
		var hashSplit = $.param.fragment().split("-");
		var hashString = "";
		for(var i=0; i<hashSplit.length-1; i++)
			hashString = hashString + hashSplit[i] + (i+1<hashSplit.length-1 ? "-" : "");
		if(hashSplit[0].substr(0,11)!="prettyPhoto")
		{
			if(hashSplit[0].substr(0,7)!="filter=")
			{
				$('.ui-accordion .ui-accordion-header#accordion-' + decodeURIComponent($.param.fragment())).trigger("change");
				$('.ui-accordion .ui-accordion-header#accordion-' + decodeURIComponent(hashString)).trigger("change");
			}
			$('.tabs .ui-tabs-nav [href="#' + decodeURIComponent(hashString) + '"]').trigger("change");
			$('.tabs .ui-tabs-nav [href="#' + decodeURIComponent($.param.fragment()) + '"]').trigger("change");
			if(hashSplit[0].substr(0,7)!="filter=")
				$('.tabs .ui-accordion .ui-accordion-header#accordion-' + decodeURIComponent($.param.fragment())).trigger("change");
			$(".testimonials-list, .our-clients-list").trigger('configuration', ['debug', false, true]);
			$(document).scroll();
		}
		if(hashSplit[0].substr(0,7)=="comment")
		{
			if($(location.hash).length)
			{
				var offset = $(location.hash).offset();
				$("html, body").animate({scrollTop: offset.top-10}, 400);
			}
		}

		// get options object from hash
		var hashOptions = $.deparam.fragment();

		if(hashSplit[0].substr(0,7)=="filter")
		{
			var filterClass = decodeURIComponent($.param.fragment()).substr(7, decodeURIComponent($.param.fragment()).length);
			// apply options from hash
			$(".isotope-filters a").removeClass("selected");
			if($('.isotope-filters a[href="#filter-' + filterClass + '"]').length)
				$('.isotope-filters a[href="#filter-' + filterClass + '"]').addClass("selected");
			else
				$(".isotope-filters li:first a").addClass("selected");

			$(".isotope").isotope({filter: (filterClass!="*" ? "." : "") + filterClass});
		}
	}).trigger("hashchange");

	$('body.dont-scroll').on("touchmove", {}, function(event){
	  event.preventDefault();
	});
	if($("#map").length)
	{
		var myMap, myPlacemark;

		ymaps.ready(init);

		function init(){
			myMap = new ymaps.Map("map", {
				center: [58.032564, 38.945141],
				zoom: 12,
				controls: ["routeEditor", 'geolocationControl', 'fullscreenControl', 'zoomControl']
			});
			myPlacemark = new ymaps.Placemark([58.032797, 38.945103], {
				hintContent: 'Наш Автосервис',
				balloonContent: 'Автосервис ИП Жолнин'
			},{ preset: 'islands#blueCarWashIcon'});
			myMap.geoObjects.add(myPlacemark)
			myMap.behaviors.disable('scrollZoom');

		}
	}
	//window resize
	function windowResize()
	{
		if(map!=null)
			map.setCenter(coordinate);
		$(".testimonials-list").trigger('configuration', ['debug', false, true]);

		if($(".re-smart-column").length && $(".header").width()>462)
		{
			var topOfWindow = $(window).scrollTop();
			$(".re-smart-column").each(function(){
				var row = $(this).parent();
				var wrapper = $(this).children().first();
				var childrenHeight = 0;
				wrapper.children().each(function(){
					childrenHeight += $(this).outerHeight(true);
				});
				if(childrenHeight<$(window).height() && row.offset().top-20<topOfWindow && row.offset().top-20+row.outerHeight()-childrenHeight>topOfWindow)
				{
					wrapper.css({"position": "fixed", "bottom": "auto", "top": "20px", "width": $(this).width() + "px"});
					$(this).css({"height": childrenHeight+"px"});
				}
				else if(childrenHeight<$(window).height() && row.offset().top-20+row.outerHeight()-childrenHeight<=topOfWindow && (row.outerHeight()-childrenHeight>0))
				{
					wrapper.css({"position": "absolute", "bottom": "0", "top": (row.outerHeight()-childrenHeight) + "px", "width": "auto"});
					$(this).css({"height": childrenHeight+"px"});
				}
				else if(childrenHeight>=$(window).height() && row.offset().top+20+childrenHeight<topOfWindow+$(window).height() && row.offset().top+20+row.outerHeight()>topOfWindow+$(window).height())
				{
					wrapper.css({"position": "fixed", "bottom": "20px", "top": "auto", "width": $(this).width() + "px"});
					$(this).css({"height": childrenHeight+"px"});
				}
				else if(childrenHeight>=$(window).height() && row.offset().top+20+row.outerHeight()<=topOfWindow+$(window).height() && (row.outerHeight()-childrenHeight>0))
				{
					wrapper.css({"position": "absolute", "bottom": "0", "top": (row.outerHeight()-childrenHeight) + "px", "width": "auto"});
					$(this).css({"height": childrenHeight+"px"});
				}
				else
					wrapper.css({"position": "static", "bottom": "auto", "top": "auto", "width": "auto"});
			});
		}
		$(".our-clients-list").each(function(){
			var self = $(this);
			self.trigger("configuration", {
				items: {
					visible: ($(".header").width()>750 ? 6 : ($(".header").width()>462 ? 4 : 2))
				},
				scroll: {
					items: ($(".header").width()>750 ? 6 : ($(".header").width()>462 ? 4 : 2))
				},
				pagination: {
					items: ($(".header").width()>750 ? 6 : ($(".header").width()>462 ? 4 : 2))
				}
			});
		});
		if($(".header").width()>300)
		{
			if(!$(".header-top-bar").is(":visible"))
				$(".header-toggle").trigger("click");
		}
		if($(".sticky").length)
		{
			if($(".header-container").hasClass("sticky"))
				menu_position = $(".header-container").offset().top;
			var topOfWindow = $(window).scrollTop();
			if(menu_position!=null && $(".header-container .sf-menu").is(":visible"))
			{
				if(menu_position<topOfWindow)
				{
					if(!$("#cs-sticky-clone").length)
						$(".header-container").after($(".header-container").clone().attr("id", "cs-sticky-clone").addClass("move"));
				}
				else
				{
					$("#cs-sticky-clone").remove();
				}
			}
			else
				$("#cs-sticky-clone").remove();
		}
	}
	$(window).resize(windowResize);
	window.addEventListener('orientationchange', windowResize);

	//scroll top
	$("a[href='#top']").on("click", function() {
		$("html, body").animate({scrollTop: 0}, "slow");
		return false;
	});

	//hint
	$(".comment-form input[type='text'], .contact-form input[type='text']:not('.cost-slider-datepicker'), .comment-form textarea, .contact-form textarea, .search input[type='text'], .search-form input[type='text'], .cost-calculator-container input[placeholder]:not('.cost-slider-datepicker')").hint();

	//reply scroll
	$(".comment-details .more").on("click", function(event){
		event.preventDefault();
		var offset = $("#comment-form").offset();
		$("html, body").animate({scrollTop: offset.top-90}, 400);
		$("#cancel-comment").css('display', 'inline');
	});

	//cancel comment button
	$("#cancel-comment").on("click", function(event){
		event.preventDefault();
		$(this).css('display', 'none');
	});

	//fancybox
	$(".prettyPhoto, [rel^='prettyPhoto']").prettyPhoto({
		show_title: false,
		slideshow: 3000,
		overlay_gallery: true,
		social_tools: ''
	});
	$("[rel^='prettyPhoto']").prettyPhoto();


	$(".submit-comment-form").on("click", function(event){
		event.preventDefault();
		$("#comment-form").submit();
	});

	//contact form
	if($(".contact-form").length)
	{
		$(".contact-form").each(function(){
			$(this)[0].reset();
			$(this).find("input[type='hidden']").each(function(){
				if(typeof($(this).data("default"))!="undefined")
					$(this).val($(this).data("default"));
			});
			$(this).find(".cost-calculator-price").costCalculator("calculate");
		});
		$(".submit-contact-form").on("click", function(event){
			event.preventDefault();
			$("#contact-form").submit();
		});
	}
	$(".contact-form").submit(function(event){
		event.preventDefault();
		var data = $(this).serializeArray();
		var self = $(this);
		//if($(this).find(".total-cost").length)
		//	data.push({name: 'total-cost', value: $(this).find(".total-cost").val()});
		self.find(".block").block({
			message: false,
			overlayCSS: {
				opacity:'0.3',
				"backgroundColor": "#FFF"
			}
		});
		$.ajax({
			url: self.attr("action"),
			data: data,
			type: "post",
			dataType: "json",
			success: function(json){
				self.find(".submit-contact-form, [name='submit'], [name='name'], [name='email'], [name='message']").qtip('destroy');
				if(typeof(json.isOk)!="undefined" && json.isOk)
				{
					if(typeof(json.submit_message)!="undefined" && json.submit_message!="")
					{
						self.find(".submit-contact-form").qtip(
						{
							style: {
								classes: 'ui-tooltip-success'
							},
							content: {
								text: json.submit_message
							},
							position: {
								my: "right center",
								at: "left center"
							}
						}).qtip('show');
						self[0].reset();
						self.find(".cost-slider-input").trigger("change");
						self.find(".cost-dropdown").selectmenu("refresh");
						self.find("input[type='text'], textarea").trigger("focus").trigger("blur");
					}
				}
				else
				{
					if(typeof(json.submit_message)!="undefined" && json.submit_message!="")
					{
						self.find(".submit-contact-form").qtip(
						{
							style: {
								classes: 'ui-tooltip-error'
							},
							content: {
								text: json.submit_message
							},
							position: {
								my: "right center",
								at: "left center"
							}
						}).qtip('show');
					}
					if(typeof(json.error_name)!="undefined" && json.error_name!="")
					{
						self.find("[name='name']").qtip(
						{
							style: {
								classes: 'ui-tooltip-error'
							},
							content: {
								text: json.error_name
							},
							position: {
								my: "bottom center",
								at: "top center"
							}
						}).qtip('show');
					}
					if(typeof(json.error_phone)!="undefined" && json.error_phone!="")
					{
						self.find("[name='phone']").qtip(
						{
							style: {
								classes: 'ui-tooltip-error'
							},
							content: {
								text: json.error_phone
							},
							position: {
								my: "bottom center",
								at: "top center"
							}
						}).qtip('show');
					}
					if(typeof(json.error_message)!="undefined" && json.error_message!="")
					{
						self.find("[name='message']").qtip(
						{
							style: {
								classes: 'ui-tooltip-error'
							},
							content: {
								text: json.error_message
							},
							position: {
								my: "bottom center",
								at: "top center"
							}
						}).qtip('show');
					}
				}
				self.find(".block").unblock();
			}
		});
	});
	var inputs = $(".contact-form-popup").find("[name='name'], [name='email'], [name='phone']");
	inputs.each(function(el){
		$(inputs[el]).on("focus", function(event){
			$(event.target).removeClass("invalid-field");
		})
	})
	//contact form popup
	if($(".contact-form-popup").length)
	{
		$(".contact-form-popup").each(function(){
			$(this)[0].reset();
			$(this).find("input[type='hidden']").each(function(){
				if(typeof($(this).data("default"))!="undefined")
					$(this).val($(this).data("default"));
			});
			$(this).find(".cost-calculator-price").costCalculator("calculate");
		});
		$(".submit-contact-form-popup").on("click", function(event){
			event.preventDefault();
			$("#contact-form-popup").submit();
		});
	}
	$(".contact-form-popup").submit(function(event){
		event.preventDefault();
		var data = $(this).serializeArray();
		var self = $(this);
		//if($(this).find(".total-cost").length)
		//	data.push({name: 'total-cost', value: $(this).find(".total-cost").val()});
		self.find(".block").block({
			message: false,
			overlayCSS: {
				opacity:'0.3',
				"backgroundColor": "#FFF"
			}
		});
		$.ajax({
			url: self.attr("action"),
			data: data,
			type: "post",
			dataType: "json",
			success: function(json){
				self.find(".submit-contact-form-popup, [name='submit'], [name='name'], [name='email'], [name='message']").qtip('destroy');
				$("p.submit-message").text(json.submit_message);
				if(typeof(json.isOk)!="undefined" && json.isOk)
				{
					if(typeof(json.submit_message)!="undefined" && json.submit_message!="")
					{
						$("p.submit-message").removeClass('invalid-field').addClass('message-sent');
						self.find("[name='name']").attr("value", 'Ваше имя*').removeClass('invalid-field');
						self.find("[name='phone']").attr("value", 'Ваш номер телефона*').removeClass('invalid-field');
					}
				}
				else
				{
					$("p.submit-message").removeClass('message-sent').addClass('invalid-field');
					if(typeof(json.submit_message)!="undefined" && json.submit_message!="")
					{
						$("p.submit-message").addClass("invalid-field");
					}
					if(typeof(json.error_name)!="undefined" && json.error_name!="")
					{
						self.find("[name='name']").attr("value",json.error_name);
						self.find("[name='name']").addClass("invalid-field");
					}
					if(typeof(json.error_phone)!="undefined" && json.error_phone!="")
					{
						self.find("[name='phone']").attr("value",json .error_phone);
						self.find("[name='phone']").addClass("invalid-field");
					}
				}
				self.find(".block").unblock();
			}
		});
	});

	if($(".header-container").hasClass("sticky"))
		menu_position = $(".header-container").offset().top;
	function animateElements()
	{
		$('.animated-element, .sticky, .re-smart-column').each(function(){
			var elementPos = $(this).offset().top;
			var topOfWindow = $(window).scrollTop();
			if($(this).hasClass("re-smart-column"))
			{
				var row = $(this).parent();
				var wrapper = $(this).children().first();
				var childrenHeight = 0;
				wrapper.children().each(function(){
					childrenHeight += $(this).outerHeight(true);
				});
				if(childrenHeight<$(window).height() && row.offset().top-20<topOfWindow && row.offset().top-20+row.outerHeight()-childrenHeight>topOfWindow)
				{
					wrapper.css({"position": "fixed", "bottom": "auto", "top": "20px", "width": $(this).width() + "px"});
					$(this).css({"height": childrenHeight+"px"});
				}
				else if(childrenHeight<$(window).height() && row.offset().top-20+row.outerHeight()-childrenHeight<=topOfWindow && (row.outerHeight()-childrenHeight>0))
				{
					wrapper.css({"position": "absolute", "bottom": "0", "top": (row.outerHeight()-childrenHeight) + "px", "width": "auto"});
					$(this).css({"height": childrenHeight+"px"});
				}
				else if(childrenHeight>=$(window).height() && row.offset().top+20+childrenHeight<topOfWindow+$(window).height() && row.offset().top+20+row.outerHeight()>topOfWindow+$(window).height())
				{
					wrapper.css({"position": "fixed", "bottom": "20px", "top": "auto", "width": $(this).width() + "px"});
					$(this).css({"height": childrenHeight+"px"});
				}
				else if(childrenHeight>=$(window).height() && row.offset().top+20+row.outerHeight()<=topOfWindow+$(window).height() && (row.outerHeight()-childrenHeight>0))
				{
					wrapper.css({"position": "absolute", "bottom": "0", "top": (row.outerHeight()-childrenHeight) + "px", "width": "auto"});
					$(this).css({"height": childrenHeight+"px"});
				}
				else
					wrapper.css({"position": "static", "bottom": "auto", "top": "auto", "width": "auto"});
			}
			else if($(this).hasClass("sticky"))
			{
				if(menu_position!=null && $(".header-container .sf-menu").is(":visible"))
				{
					if(menu_position<topOfWindow)
					{
						//$(this).addClass("move");
						if(!$("#cs-sticky-clone").length)
							$(this).after($(this).clone().attr("id", "cs-sticky-clone").addClass("move"));
					}
					else
					{
						//$(this).removeClass("move");
						$("#cs-sticky-clone").remove();
					}
				}
			}
			else if(elementPos<topOfWindow+$(window).height()-20)
			{
				if($(this).hasClass("number") && !$(this).hasClass("progress") && $(this).is(":visible"))
				{
					var self = $(this);
					self.addClass("progress");
					if(typeof(self.data("value"))!="undefined")
					{
						var value = parseFloat(self.data("value").toString().replace(" ",""));
						self.text(0);
						self.text(value);
					}
				}
				else if(!$(this).hasClass("progress"))
				{
					var elementClasses = $(this).attr('class').split(' ');
					var animation = "fadeIn";
					var duration = 600;
					var delay = 0;
					if($(this).hasClass("scroll-top"))
					{
						if(topOfWindow<$(document).height()/2)
						{
							if($(this).hasClass("fadeIn") || $(this).hasClass("fadeOut"))
								animation = "fadeOut";
							else
								animation = "";
							$(this).removeClass("fadeIn")
						}
						else
							$(this).removeClass("fadeOut")
					}
					for(var i=0; i<elementClasses.length; i++)
					{
						if(elementClasses[i].indexOf('animation-')!=-1)
							animation = elementClasses[i].replace('animation-', '');
						if(elementClasses[i].indexOf('duration-')!=-1)
							duration = elementClasses[i].replace('duration-', '');
						if(elementClasses[i].indexOf('delay-')!=-1)
							delay = elementClasses[i].replace('delay-', '');
					}
					$(this).addClass(animation);
					$(this).css({"animation-duration": duration + "ms"});
					$(this).css({"animation-delay": delay + "ms"});
					$(this).css({"transition-delay": delay + "ms"});
				}
			}
		});
	}
	setTimeout(animateElements, 1);
	$(window).scroll(animateElements);
});
