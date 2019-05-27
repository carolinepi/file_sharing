function upload(event) {
    event.preventDefault();
    var data = new FormData($('form').get(0));

    $.ajax({
        url: $(this).attr('data-url'),
        type: $(this).attr('method'),
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: handleSuccess(data),
        error: handleError,
    });
    return false;
}

function handleSuccess(data){
    $("form")[0].reset();
//    alert('Success uploading!');
}

function handleError(ThrowError){
    console.log(ThrowError);
    alert('Please, log in or sign up!');
}

$(function() {
    $('form').submit(upload);
});