function ajax_insert(item){
    btn_html = "<center><button type='btn' class='buttons' id='edit' onclick=\"edit(" + item.id + ", '" + item.name + "', " + item.order_qty + ", '" + item.cossh + "');\"><img src='" + $SCRIPT_ROOT + "/static/open-iconic-master/svg/pencil.svg' alt='pencil'></button><center>";
    html = "<tr><td>" + item.name + "</td><td> " + item.id + "</td><td>" + item.order_qty + "</td><td><a href=" + item.cossh + ">" + item.cossh + "</a></td><center><td>" + btn_html + "</td></center>";
    return html;
}
$(function() {
    ajax_return("product_list");
});

function edit(id, name, address){
    $('#modal-title').text(name);
    $('#modal_edit').modal('show');
    
}

function ajax_follow(){

}