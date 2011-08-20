$(document).ready(function (){
	var wrapper = $('#doc-wrapper');
	var col1 = $('#col1', wrapper);
	var col2 = $('#col2', wrapper);
	var expand = $('#expand-col1', col1);
	var _fadespeed = 300;
	
	var col1norm = col1.width();
	var col1grow = col1norm + (wrapper.width() - col1.outerWidth());
	
	expand
		.text('Expand')
		.css('left', (col1.outerWidth() - expand.outerWidth() - 3) + 'px')
		.show();
	
	expand.live('click', function(){
		var vis = col2.is(':visible');
		expand.animate({opacity:'0.0'}, _fadespeed);
		
		if (vis)
		{
			col2.hide();
		}
		
		col1.animate({ width: (vis ? col1grow : col1norm) + 'px'}, {
		    duration: 200,
		    specialEasing: { width: 'easeOutExpo'},
		    complete: function () {
		    	expand
	    			.text(vis ? 'Collapse' : 'Expand')
		    		.css('left', (col1.outerWidth() - expand.outerWidth() - 3) + 'px')
		    		.animate({opacity:'1.0'}, _fadespeed); 
		    	}
		  });
		
		if (!vis)
		{
			col2.show();
		}		
	});
});