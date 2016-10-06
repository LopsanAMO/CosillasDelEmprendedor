$.noConflict();

jQuery(document).ready(function(){
	setTimeout(function(){
		resizeImg();
	}, 300);
	
	jQuery(window).resize(function(){
		resizeImg();
	});

	jQuery('.slider_container').each(function(){
		var selector = jQuery(this);
		var items_length = jQuery(this).find('.slider_item').length;
		var initCarousel = setInterval( function(){ slider(selector, items_length) }, 7000 );
	});

	jQuery('#search_bar').keyup(function(){
		if ( jQuery(this).val() == '' || jQuery(this).val() == null ) {
			jQuery('#search_bar_hidden_list').hide();
		}
		else {
			jQuery('#search_bar_hidden_list').slideDown(function(){
				resizeImg();
			});	
		}
		
	});
		
});

function resizeImg(){
	jQuery('img').each(function(){

		var width = parseFloat(jQuery(this).parent().css('width'));
		var height = parseFloat(jQuery(this).parent().css('height'));
		var parentProp = width/height;
		var imgProp = parseFloat(jQuery(this).css('width'))/parseFloat(jQuery(this).css('height'));

		if ( parentProp > 1 ) {
			if ( imgProp > 1 ) {
				if ( imgProp > parentProp ) {
					jQuery(this).removeClass('w_100').addClass('h_100');
				}
				else{
					jQuery(this).removeClass('h_100').addClass('w_100');	
				}
			}
			else {
				jQuery(this).removeClass('w_100').addClass('h_100');	
			}
		}
		else if ( parentProp < 1 ) {
			if ( imgProp > 1 ) {
				jQuery(this).removeClass('w_100').addClass('h_100');
			}
			else {
				jQuery(this).removeClass('h_100').addClass('w_100');	
			}
		}

	});
}

var increment = 1;
function slider(selector, items_length){
	selector.find('.slider_item').fadeOut();
	selector.find('.slider_item').eq(increment).fadeIn(1500);

	if ( increment < items_length - 1) {
		increment++;
	}
	else {
		increment = 0;
	}

}