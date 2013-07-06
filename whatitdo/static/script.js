// Main script for what.it.do

$(document).ready(function(){

	// hide drawers - visible by default in case Javascript is off
	// $('.drawer').hide();

	// fade demo blurb in
	$('#demoblurb').ready(function() {
		$('#demoblurb').hide();
		$('#demoblurb').delay(300).fadeIn(1000);
	});

	// show/hide individual drawers
	$('.morecol').click(function(){
		if ($(this).hasClass('is_open')) {
			$(this).next().fadeToggle(0);
			$(this).removeClass('is_open');
			return;
		}
		$(this).next().fadeToggle(300);
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
		$('.drawer').fadeOut(0).fadeToggle(300);
		$(this).addClass('all_open');
		$('.morecol').addClass('is_open');
	});

});
