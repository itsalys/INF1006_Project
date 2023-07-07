$(document).ready(function() {
    var start_status = $('#livlighttoggle').is(':checked');
    if(start_status){
      $("#lrlightstatus").text('The living room light is turned On');
    }
    else{
      $("#lrlightstatus").text('The living room light is turned Off');
    }

    $('#livlighttoggle').click(function() {
      var isChecked = $('#livlighttoggle').is(':checked');
      console.log('isChecked: ', isChecked);
      $.ajax({
        type: 'POST',
        url: '/process_LRLight_Toggle',
        data: { status: isChecked },
        success: function(response) {
          $("#lrlightstatus").text(response.msg);
        },
        error: function(xhr) {
          console.log(xhr.statusText);
        }
      });
    });
});