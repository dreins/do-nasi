
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
  console.log("ok")
}


// $(document).ready(function() {
//   $('#description').summernote();
// });
function load() {

  console.log("ok1")
  // FETCHING DATA FROM JSON FILE
  $.getJSON("./json/article",
    function (data) {
      var task = '';

      // ITERATING THROUGH OBJECTS
      $.each(data, function (key, value) {

        var fulltext = value.fields.body;
        var shorttext = jQuery.trim(fulltext).substring(0, 450)
          .split(" ").join(" ") + "...";

        task += '<div class="card">';
        task += '<div class="card-body">';
        task += '<h5 class="card-title">' + value.fields.title + '</h5>';
        task += '<p class="card-text">' + shorttext + '</p>';
        task += ' <a href="' + value.fields.slug + '" class="read-more">Read more</a>';
        task += '</div>';
        task += '</div>';


      });

      //INSERTING ROWS INTO TABLE 
      $('.container').append(task);

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
  bodyField()

  // $('#form-add').submit(function (e) {
  //   e.preventDefault();

    // console.log("ok2")
    // var data = JSON.stringify($("#form-add").serializeJSON())
    // // data = JSON.parse(data)
    // console.log("data", data)

    // $.ajax({
    //   type: 'POST',
    //   url: "/add-article/",
    //   dataType: "json",
    //   data: {
    //     action: 'post',
    //     title: $('#title').val(),
    //     body: $('#description').val(),
    //     slug: $("#slug").val(),
    //     data: data,
    //     // csrfmiddlewaretoken: '{{ csrf_token }}'
    //     csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    //   },
      
    //   success: function (json) {
    //     document.getElementById("form-add").reset();
    //     var slug = json.description;
    //     var slugtitle = jQuery.trim(slug).split(" ").join("-");

    //     $(".container").prepend('<div class="card">' +
    //       '<div class="card-body">' +
    //       '<h5 class="card-title">' + json.title + '</h5>' +
    //       '<p class="card-text">' + slugtitle + '</p>' +
    //       ' <a href="' + json.slug + '" class="read-more">Read more</a>' +
    //       '</div>' +
    //       '</div>'
    //     )
    //   },
    //   error: function (xhr, errmsg, err) {
    //     console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    //   }
    // });
  // });
});
