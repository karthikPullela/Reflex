$(document).ready(function() {
    
    $('body').css('display','none');
	$(document).ready(function() {
		$('body').fadeIn(1000);
		$('a').on('click',function(event){
			var thetarget = this.getAttribute('target')
			if (thetarget != "_blank"){			
				var thehref = this.getAttribute('href')
				event.preventDefault();
				$('body').fadeOut(function(){
					//alert(thehref)
					window.location = thehref			
				});
			}
		});
	});
	setTimeout(function(){
		$('body').fadeIn();
	},1000)
});


