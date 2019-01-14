$(function() {
    status = ""
    stat_class = ""
    
    
    //Pulling site JSON data from route, add to drop down
    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + "sites_list",
        dataType: 'json',
        success: function (data) {
            var html = '';
            $.each(data, function (i, item) {

                html += "<option value='" + item.id + "'>" + item.name + "</option>"
            });
            $('#sites').append(html);
            
        }
    });
    $('#modal_init').modal('show');
    
    //Add search functionality to search bar
    $("#search").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#stock tbody tr").filter(function() {
    $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
});
});
});

function load_stock(){
    site = $("#sites").val();
    $('#modal_init').modal('hide');
    out_btn_state = "btn_enabled";
    low_btn_state = "btn_enabled";
    
    //Pull stock JSON from route
    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + "stock_list",
        dataType: 'json',
        success: function (data) {
            var html = '';
            status = "";
            console.log(low_btn_state)
            $.each(data, function (i, item) {
                if (item.site_id == site){
                    console.log(item.stock_healthy)
                    if (item.stock_healthy == 1){
                        status = "Normal";
                        colour = "#28a745"; 
                        out_btn_state = "btn_enabled";
                        low_btn_state = "btn_enabled";
                        console.log("Normal")
                    }
                    else if (item.stock_healthy ==  null){
                        status = "Ordered";
                        colour = "#dc3545";
                        out_btn_state = "btn_disabled"
                        low_btn_state = "btn_disabled";
                        console.log("out")
                    }
                    else if (item.stock_healthy == 0){
                        status = "Low";
                        colour = "#ffc107";
                        low_btn_state = "btn_disabled";
                        out_btn_state = "btn_enabled";
                        console.log("low")
                    }
                   
                    console.log(low_btn_state)
                    btns_html = "<center><div class='btn-group' role='group'><button type='button' onclick='confirm(" + item.id + ", false);' class='btn btn-warning " + low_btn_state + "'>Low</button><button type='button' onclick='confirm(" + item.id + ", undefined);' class='btn btn-danger " + out_btn_state + "'>Out</button></div></center>"
                    html += "<tr><td>" + item.name + "</td>center><td class='status' style='background-color: " + colour + ";'>" + status + "</td></center><td>" +  btns_html;
                }
            });
            //Append every stock item to the table          
            $('#stock tbody').append(html);
            $(".btn_disabled").attr("disabled", true);
        }
        
    });
    

}
function confirm(id, to_status){
    //Pass the item id and the change as parameters the set_stock function if confirmed
    $(".change").attr("onclick","set_stock(" + id + ", " + to_status +")");
    
    $('#modal_confirm').modal('show');
}

function set_stock(id, to_status){
    $.ajax({
        type:  "GET",
        url: $SCRIPT_ROOT + "change_stock",
        data: {id: id, to_status: to_status},

        success: function(data){
            $("#stock tbody tr").remove();
            load_stock()
    }
    
    });
}