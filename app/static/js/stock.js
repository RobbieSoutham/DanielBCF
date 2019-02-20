function ajax_insert(item, route){
    console.log(item.id);
    if (route == "sites_list"){
        html = "<option value='" + item.name + "'>" + item.name + "</option>";
        return html;
    }
    else if (route == "stock_list"){
        status = ""
        stat_class = ""
        site = $("#sites").val();
        out_btn_state = "btn_enabled";
        low_btn_state = "btn_enabled";
        html = '';
        status = "";
        if (item.site_id == site){
            if (item.stock_healthy == 1){
                status = "Normal";
                colour = "#28a745"; 
                out_btn_state = "btn_enabled";
                low_btn_state = "btn_enabled";
            }
            else if (item.stock_healthy ==  null){
                status = "Ordered";
                colour = "#dc3545";
                out_btn_state = "btn_disabled"
                low_btn_state = "btn_disabled";
            }
            else if (item.stock_healthy == 0){
                status = "Low";
                colour = "#ffc107";
                low_btn_state = "btn_disabled";
                out_btn_state = "btn_enabled";
            }
            console.log("sdfsdfsdf");
            btns_html = "<td><center><div class='btn-group' role='group'><button type='button' onclick='confirm(" + item.id + ", false);' class='btn btn-warning " + low_btn_state + "'>Low</button><button type='button' onclick='confirm(" + item.id + ", undefined);' class='btn btn-danger " + out_btn_state + "'>Out</button></div></center></td>"
            html = "<tr><td class='name'>" + item.name + "</td>center><td class='status' style='background-color: " + colour + ";'>" + status + "</td></center>" +  btns_html;
            return html;
        }
    }
}
$(function() {
    ajax_return("sites_list", "#sites");
    $('#modal_init').modal('show');
});

function load_content(){
    $('#modal_init').modal('hide');
    
    //Pull stock JSON from route
    ajax_return("stock_list", "tbody");

}

function ajax_follow(){
    //Disable buttons with the disabled class
    $(".btn_disabled").attr("disabled", true);
}
function confirm(id, to_status){

    //Pass the item id and the change as parameters the set_stock function if confirmed
    $(".change").attr("onclick","ajax_change('change_stock', {id: " + id + ", to_status: '" + to_status + "'});");  
    $('#modal_confirm').modal('show');
}
