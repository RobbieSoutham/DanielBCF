$(function() {
    
    //Pulling site JSON data from route, add to drop down
    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + "products_list",
        dataType: 'json',
        success: function (data) {
            var html = '';
            $.each(data, function (i, item) {

                html += "<option value='" + item.id + "'>" + item.name + "</option>"
            });
            $('#products').append(html);
            
        }
    });
});