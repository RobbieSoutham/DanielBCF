$(function() {
    status = ""
    stat_class = ""
    
    $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};

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

    $('.modal').modal('show');
});

function loadSites(){
    site = $("#sites").val();
    $(".modal").remove();
    $(".modal-backdrop").remove();
    $("body").removeClass( "modal-open" );

    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + "stock_list",
        dataType: 'json',
        success: function (data) {
            var html = '';
            status = "";
            $.each(data, function (i, item) {
                if (item.site_id == site){
                
                    if (item.stock_healthy == 1){
                        status = "Normal";
                        colour = "#28a745"
                    }
                    else if (items.stock_healthy == 0){
                        status = "Low"
                        colour = "##ffc107"

                    }
                    else{
                        status = "Ordered"
                        colour = "#dc3545"
                    }

                    btns_html = "<center><div class='btn-group' role='group'><button type='button' id='stock_change' class='btn btn-warning'>Low</button><button type='button' id='stock_change' class='btn btn-danger'>Out</button></div></center>"

                    html += "<tr><td>" + item.name + "</td>center><td class='status' style='background-color: " + colour + ";'>" + status + "</td></center><td>" +  btns_html;
                }
            });
            $('#stock').append(html);
        }
        });
}