// Main script for what.it.do

$(document).ready(function(){

	// hide drawers - visible by default in case Javascript is off
	$('.comment').fadeOut(0);
	$('.drawer').hide();

	// show/hide individual drawers
	$('.morecol').click(function(){
		if ($(this).hasClass('is_open')) {
			$(this).next().toggle();
			$(this).next().contents().fadeOut(0);
			$(this).removeClass('is_open');
			return;
		};
		$(this).next().toggle();
		$(this).next().contents(':hidden').fadeIn(350);
		$(this).addClass('is_open');
	});

	// show/hide all drawers
	$('.listhead.morecol').click(function(){
		if ($(this).hasClass('all_open')) {
			$('.drawer').hide();
			$('.drawer').children().fadeOut(0);
			$(this).removeClass('all_open');
			$('.morecol').removeClass('is_open');
			return;
		};
		$('.drawer').show();
		$('.drawer').children(':hidden').fadeIn(350);
		$(this).addClass('all_open');
		$('.morecol').addClass('is_open');
	});

});

