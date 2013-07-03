// Main script for what.it.do

$(document).ready(function(){

	// hide drawers - visible by default in case Javascript is off
	$('.drawer').children().hide;
	$('.drawer').hide();

	// fade demo blurb in
	$('#demoblurb').hide();
	$('#demoblurb').delay(300).fadeIn(1000);


	// show/hide individual drawers
	$('.morecol').click(function(){
		if ($(this).hasClass('is_open')) {
			$(this).next().toggle();
			$(this).next().children().fadeOut(0);
			$(this).removeClass('is_open');
			return;
		}
		$(this).next().toggle();
		if ($(window).width() > 888 ) {
			$(this).next().contents(':hidden').fadeIn(350); }
		else {$(this).next().contents(':hidden').show(); }

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
		}
		$('.drawer').show();
		if ($(window).width() > 888 ) {
			$('.drawer').children(':hidden').fadeIn(350); }
		else {$('.drawer').children(':hidden').show();}
		$(this).addClass('all_open');
		$('.morecol').addClass('is_open');
	});

});

