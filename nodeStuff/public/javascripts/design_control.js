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
		var initCarousel = setInterval( function(){ slider(selector, items_length); }, 7000 );
	});

	/*jQuery('#search_bar').keyup(function(){
		if ( jQuery(this).val() == '' || jQuery(this).val() == null ) {
			jQuery('#search_bar_hidden_list').hide();
		}
		else {
			jQuery('#search_bar_hidden_list').slideDown(function(){
				jQuery.ajax({
					method: 'GET'
				})
			});
		}

	});*/

	var client = algoliasearch('18FVHAVRWL', 'b12d5c50d36b45ea98d61b0f3cea4e7f');
	var index = client.initIndex('Lugares');
	jQuery('#search_bar').autocomplete({ hint: false }, [
		{
			source: jQuery.fn.autocomplete.sources.hits(index, { hitsPerPage: 5 }),
			displayKey: 'nombre',
			templates: {
				suggestion: function(suggestion) {
					if(jQuery('#search_bar').val() === ''){
							jQuery('#search_bar_hidden_list').hide();
					}
					else {
						jQuery('#search_bar_hidden_list').show();
						jQuery('#search_bar_result').html('');
						jQuery('#search_bar_result').append(
								'<div class="col-md1 list searchbar_list bg_white">' + '\n' +
							  '<div class="col-md1 list_item hover_item selectable">' + '\n' +
							  '<div class="item_img"><img src="http://www.wikimexico.com/storage/app/uploads/public/559/98a/eb4/55998aeb4b3e8171992098.jpg"/></div><!--' + '\n' +
							  '--><div class="item_info">' + '\n' +
							  '    <div class="layout_padding_hmax">' + '\n' +
							  '      <h3 class="layout_margin_bottom_min">' + suggestion._highlightResult.nombre.value + '</h3>' + '\n' +
							  '      <div class="col-md1 txt_density_bold font_color_light">Descripcion</div>' + '\n' +
							  '      <div class="col-md1">' + 'Hola' +'</div>' + '\n' +
							  '    </div>' + '\n' +
							  '  </div>' + '\n' +
							  '</div>' + '\n' +
							'</div>'
						);
						resizeImg();
					}
				}
			}
		}
	]).on('autocomplete:selected', function(event, suggestion, dataset) {
		console.log(suggestion, dataset);
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
