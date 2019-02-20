function ajax_insert(item){
    btn1 = "<button type='btn' class='buttons' id='edit' onclick=\"edit('" + item.id + "', '" + item.name + "', " + item.order_qty + ", '" + item.cossh + "');\"><img src='" + $SCRIPT_ROOT + "/static/open-iconic-master/svg/pencil.svg' alt='pencil'></button>";
    btn2 = "<button class='buttons' id='delete' onclick='delete_product(\"" + item.id + "\");'><img src='" + $SCRIPT_ROOT + "/static/open-iconic-master/svg/x.svg' alt='x'></button><center>";
    html = "<tr><td>" + item.name + "</td><td> " + item.id + "</td><td>" + item.order_qty + "</td><td><a href=" + item.cossh + ">" + item.cossh + "</a></td><td><center>" + btn1 + btn2 + "<center></td>";
    return html;
}
$(function() {
    ajax_return("product_list");
    $("#edit").parent().css("display", "none");
    $("#previous_id").parent().css("display", "none");
});

function edit(id, name, order_qty, cossh){
    $('input[type="checkbox"]').prop("checked", true);
    $('#previous_id').val(id);
    $('#modal-title').text(name);
    $('#name').val(name);
    $('#product_id').val(id);
    $('#order_qty').val(order_qty);
    $('#cossh').val(cossh);
    $('#modal').modal('show');
    
}

function reset_modal(){
    $('input[type="checkbox"]').prop("checked", false);
    $('#modal-title').text("Add Product");
    $('#name').val("");
    $('#product_id').val("");
    $('#order_qty').val("");
    $('#cossh').val("");
    $('#modal').modal('hide');
}
function ajax_follow(){

}

function delete_product(id){
    ajax_change("delete_product", {"id": "'" + id + "'"});
    load_content();
}

function load_content(){
    $("td").remove();
    ajax_return("product_list");
}