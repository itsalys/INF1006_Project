$(document).ready(function() {

    //For Light Toggle Default Display
    var start_status = $('#livlighttoggle').is(':checked');
    if(start_status){
      $("#lrlightstatus").text('The living room light is turned On');
    }
    else{
      $("#lrlightstatus").text('The living room light is turned Off');
    }

    //For Fan Toggle Default Display
    var curr_status = $('#livfantoggle').is(':checked');
    if(curr_status){
      $("#lrfanstatus").text('The living room fan is turned On');
    }
    else{
      $("#lrfanstatus").text('The living room fan is turned Off');
    }

    //For Light Toggle Clicked
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

    //For Fan Toggle Clicked
    $('#livfantoggle').click(function() {
      var isChecked = $('#livfantoggle').is(':checked');
      console.log('isChecked: ', isChecked);
      $.ajax({
        type: 'POST',
        url: '/process_LRFan_Toggle',
        data: { status: isChecked },
        success: function(response) {
          $("#lrfanstatus").text(response.msg);
        },
        error: function(xhr) {
          console.log(xhr.statusText);
        }
      });
    });

});