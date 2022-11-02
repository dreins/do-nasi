function convertToSlug(str) {

  //replace all special characters | symbols with a space
  str = str.replace(/[`~!@#$%^&*()_\-+=\[\]{};:'"\\|\/,.<>?\s]/g, ' ')
    .toLowerCase();

  // trim spaces at start and end of string
  str = str.replace(/^\s+|\s+$/gm, '');

  // replace space with dash/hyphen
  str = str.replace(/\s+/g, '-');
  document.getElementById("slug").innerHTML = str;
  //return str;
}

function bodyField() {
  $('#description').summernote();
}



// $(document).ready(function() {
//   $('#description').summernote();
// });
function load() {

  // FETCHING DATA FROM JSON FILE
  $.getJSON("./json/article",
    function (data) {
      var article = '';

      // ITERATING THROUGH OBJECTS
      $.each(data, function (key, value) {

        var fulltext = value.fields.body;
        var shorttext = jQuery.trim(fulltext).substring(0, 450)
          .split(" ").join(" ") + "...";

        article += '<div class="card">';
        article += '<div class="card-body">';
        article += '<h5 class="card-title">' + value.fields.title + '</h5>';
        article += '<p class="card-text">' + shorttext + '</p>';
        article += ' <a href="' + value.fields.slug + '" class="read-more">Read more</a>';
        article += '</div>';
        article += '</div>';


      });

      //INSERTING CARD
      document.getElementById('container').innerHTML = article;

    });
}



//   $('#title').keyup(function(){
//   var str =$(this).val();
//   var trims =$.trim(str)
//   var slug = trims.replace(/[^a-z0-9]/gi, '-').replace(/-+/g, '-').replace( /^-|-$/g, '')
//   $("#slug").val(slug.toLowerCase()+".html")
// })

$(document).ready(function () {
  load();
  bodyField();

  $('#form-add').submit(function (e) {
    e.preventDefault();

  
    $.ajax({
      type: 'POST',
      url: "add_article/",
      dataType: "json",
      data: {
        action: 'post',
        title: $('#title').val(),
        body: $('#description').val(),
        slug: $("#slug").val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
      },
      
      success: function (json) { 
        document.getElementById("form-add").reset();
        $('#description').summernote('reset');
        $("#slug").val("");
        

        // var slug = json.description;
        // var slugtitle = jQuery.trim(slug).split(" ").join("-");

        load();
        // $(".container").prepend('<div class="card">' +
        //   '<div class="card-body">' +
        //   '<h5 class="card-title">' + json.title + '</h5>' +
        //   '<p class="card-text">' + slugtitle + '</p>' +
        //   ' <a href="' + json.slug + '" class="read-more">Read more</a>' +
        //   '</div>' +
        //   '</div>'
        // )
      },
      error: function (xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
    });
  });
});
