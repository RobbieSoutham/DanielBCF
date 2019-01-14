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
                    
                    html += "<tr><td>" + item.name + "</td>center><center><td> " + item.id + "</td></center><td><center>" + item.order_qty + "</td></center><td><center><a>" + item.cossh + "</a></td></center><center><td><img src='" + $SCRIPT_ROOT + "/static/open-iconic-master/svg/account-login.svg' alt='account login'></td></center>";
                
            });
            console.log(html)
            //Append every product item to the table          
            $('#products tbody').append(html);
        }
        
    });
});