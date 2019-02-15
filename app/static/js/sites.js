function ajax_insert(item){
    bttn_html = "<center><button type='button' class='buttons' id='edit' onclick='edit(" + item.id + ", \"" + item.name + "\");'><img src='" + $SCRIPT_ROOT + "/static/open-iconic-master/svg/pencil.svg' alt='pencil'></button><center>"; 
    html = "<tr><td>" + item.name + "</td><center><center><td> " + item.address + "</td></center><td><center>" + bttn_html + "</td></center>";
    return html;
}

$(function() {
    ajax_return("sites_list");
});


function edit(id, name, order_qty, cossh){
    $('#modal-title').text(name);
    $('#modal_edit').modal('show');
    
}