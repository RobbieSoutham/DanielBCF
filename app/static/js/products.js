$(function() {
    
    //Pulling site JSON data from route, add to drop down
    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + "product_list",
        dataType: 'json',
        success: function (data) {
            var html = '';
            status = "";
            $.each(data, function (i, item) {
                    
                    html += "<tr><td>" + item.id + "</td>center><center><td><</td></center><td>";
                
            });
            console.log(html)
            //Append every product item to the table          
            $('#products tbody').append(html);
        }
        
    });
});