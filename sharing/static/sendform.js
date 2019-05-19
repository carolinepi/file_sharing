$(document).ready(function(){

	var $uploadForm = $('.form-upload');
	$uploadForm.submit(function(event){
		event.preventDefault();
		var $formData = $uploadForm.serialize();
		var $thisURL = $uploadForm.attr('data-url') || window.location.href;
		$.ajax({
			method:'POST',
			url: $thisURL,
			data: $formData,
			success: handleSuccess,
			error: handleError,
		});
        function handleSuccess(data){
			console.log(data.message);
			$uploadForm[0].reset()
		}
		function handleError(ThrowError){
			console.log(ThrowError);
		}
	});
});