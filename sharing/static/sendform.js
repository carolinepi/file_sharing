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
    alert('Success uploading!');
//    data.reset()
}
function handleError(ThrowError){
    console.log(ThrowError);
}

$(function() {
    $('form').submit(upload);
});