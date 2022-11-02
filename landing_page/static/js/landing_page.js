function load_data() {
    $.ajax({
        url: './penyalur-json/.',
        dataType: 'json',
        data: '{{ list }}',
        success: function (data) {
            if(data.length == 0) {
                $( "#show" ).hide();
            } else {
                $( "#show" ).click(function() {
                    show(data);
                });  
            }             
        },
        error: function(jqXHR, textStatus, errorThrown) {
            alert('Error: ' + textStatus + ' - ' + errorThrown);
        }
    });
}
function show(data) {
    var donasi = '<ul>';
    for (var i = 0; i < data.length; i++) {
        donasi += '<li>';
        donasi += data[i].fields.title;
        donasi += '</li>';
    }
    donasi += '</ul>';
    document.getElementById('daftar-donasi').innerHTML = donasi; 
    $("#show").hide();    
    $("#hide").show();
    $("#daftar-donasi").show();            
}

function hide() {
    $("#show").show();    
    $("#hide").hide(); 
    $("#daftar-donasi").hide(); 
}

$(document).ready(function() {
    $("#hide").hide();
    $.ajax({
        url: './penyalur-json/.',
        dataType: 'json',
        data: '{{ list }}',
        success: function (data) {    
            document.getElementById('jumlah').innerHTML = data.length;                
        },
        error: function(jqXHR, textStatus, errorThrown) {
            alert('Error: ' + textStatus + ' - ' + errorThrown);
        }
    });
});