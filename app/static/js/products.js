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
                    btn_html = "<center><button type='btn' id='edit' onclick=\"edit(" + item.id + ", '" + item.name + "', " + item.order_qty + ", '" + item.cossh + "');\"><img src='" + $SCRIPT_ROOT + "/static/open-iconic-master/svg/pencil.svg' alt='pencil'></button><center>";
                    html += "<tr><td>" + item.name + "</td>center><center><td> " + item.id + "</td></center><td><center>" + item.order_qty + "</td></center><td><center><a href=" + item.cossh + ">Link</a></td></center><center><td>" + btn_html + "</td></center>";
                
            });
            console.log(btn_html)
            //Append every product item to the table          
            $('#products tbody').append(html);
        }
        
    });
});

function edit(id, name, order_qty, cossh){
    $('#modal-title').text(name);
    $('#modal_edit').modal('show');
    
}