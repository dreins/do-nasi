
  function convertToSlug( str ) {
    
    //replace all special characters | symbols with a space
    str = str.replace(/[`~!@#$%^&*()_\-+=\[\]{};:'"\\|\/,.<>?\s]/g, ' ')
             .toLowerCase();
      
    // trim spaces at start and end of string
    str = str.replace(/^\s+|\s+$/gm,'');
      
    // replace space with dash/hyphen
    str = str.replace(/\s+/g, '-');   
    document.getElementById("slug").innerHTML = str;
    //return str;
  }

  $(document).ready(function() {
    $('#description').summernote();
  });

  $(document).ready(function () {

      // FETCHING DATA FROM JSON FILE
      $.getJSON("./json/article", 
              function (data) {
          var task = '';

          // ITERATING THROUGH OBJECTS
          $.each(data, function (key, value) {

              var fulltext = value.fields.body;
              var shorttext = jQuery.trim(fulltext).substring(0, 450)
                              .split(" ").join(" ") + "...";
                              
              task+='<div class="card">';
              task+='<div class="card-body">';
              task+='<h5 class="card-title">'+value.fields.title+'</h5>';
              task+='<p class="card-text">'+shorttext+'</p>';
              task+=' <a href="'+value.fields.slug+'" class="read-more">Read more</a>';
              task+='</div>';
              task+='</div>'; 
              

          });
            
          //INSERTING ROWS INTO TABLE 
          $('.container').append(task);
          
      });
  });
  
    $('#title').keyup(function(){
    var str =$(this).val();
    var trims =$.trim(str)
    var slug = trims.replace(/[^a-z0-9]/gi, '-').replace(/-+/g, '-').replace( /^-|-$/g, '')
    $("#slug").val(slug.toLowerCase()+".html")
  })



