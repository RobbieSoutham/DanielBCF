function ajax_return(route, append_to = "tbody"){
    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + route,
        dataType: "json",
        success: function (data) {
            var html = "";
            status = "";
            $.each(data, function (i, item) {
                html += ajax_insert(item, route);
            });

            //Append every item to the table          
            $(append_to).append(html);
            
            ajax_follow();
        }
    });
    
}

function ajax_change(route, data){
    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + route,
        data: data,

        success: function(data){
            $("td").remove();
            load_content();
            
        }
        
    });
}

function ajax_submit(page){
    $("form").submit();
    $.ajax({
        type: "POST",
        url: $SCRIPT_ROOT + "/modal_forms",
        dataType: "json",
        #Send page with form to distinguish between forms
        data: $("form").serialize() + "&page=" + page,
    
        success: function (data) {
            if (data == true){
                //Update table
                reset_modal();
                load_content();

                //Remove error alert if shown
                $(".alert").remove();
            }
            else{
                //Adding error message like flash with the error obtained from route
                html = "<ul class='errors alert alert-danger'><li>" + data + "</li></ul>"
                $("body").append(html)
            }
        }

      });
    }
