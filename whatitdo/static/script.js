"use strict";

function turnOnButton() {
	var category = $('div.list').attr('data-category');
	if ($.inArray(category, ['tv', 'movies', 'books', 'games', 'music']) > -1) {
		var buttoncls = "." + category + "button";
		$(buttoncls).removeClass('buttonoff').addClass('buttonon');
	}
}

function fadeInDemoBlurb() {
	$('#demoblurb').ready(function() {
		$('#demoblurb').hide();
		$('#demoblurb').delay(300).fadeIn(1000);
	});
}

function setupDrawerClick() {
	// show/hide individual drawers
	$('.morecol').click(function(){
		if ($(this).hasClass('is_open')) {
			$(this).next().fadeToggle(0);
			$(this).removeClass('is_open');
			return;
		}
		$(this).next().fadeToggle(200);
		$(this).addClass('is_open');
	});

	// show/hide all drawers
	$('.listhead.morecol').click(function(){
		if ($(this).hasClass('all_open')) {
			$('.drawer').fadeIn(0).fadeToggle(0);
			$(this).removeClass('all_open');
			$('.morecol').removeClass('is_open');
			return;
		}
		$('.drawer').fadeOut(0).fadeToggle(200);
		$(this).addClass('all_open');
		$('.morecol').addClass('is_open');
	});	
}

$(document).ready(function(){
	turnOnButton();
	fadeInDemoBlurb();
	setupDrawerClick();	
});
