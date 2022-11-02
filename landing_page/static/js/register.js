$(document).on('submit', '#form', function(e){
    $(".alert").hide();
    e.preventDefault();
    
    var form_data = $('#form')

    $.ajax({
        type: 'POST',
        url: '',
        data: form_data.serialize(),
        dataType: "json",
        header: {'X-CSRFToken': '{% csrf_token %}'},
        success: function(response){
        var success = response['success']
        if (success){
            $(".alert-success").show();
        }
        else {
            $(".alert-danger").show();
            for(var msg in response['error']) {
            var txt = JSON.stringify(response['error'][msg]);
            document.getElementById("error").innerHTML = txt.replace(/[&\/\\#,\]+()$~%['":*?<>{}]/g, '');
            }
        }
        },
    });
});

$(document).ready(function(){
    $(".alert").hide();
});