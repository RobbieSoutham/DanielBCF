function ajax_return(route, append_to = "tbody"){
    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + route,
        dataType: 'json',
        success: function (data) {
            var html = '';
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
        type:  "GET",
        url: $SCRIPT_ROOT + route,
        data: data,

        success: function(data){
            $("td").remove();
            load_content();
            
        }
        
    });
}