function ajax_insert(item){
    bttn_html = "<center><button type='button' class='buttons' id='edit' onclick='edit(" + item.id + ", \"" + item.name + "\", \"" + item.address + "\");'><img src='" + $SCRIPT_ROOT + "/static/open-iconic-master/svg/pencil.svg' alt='pencil'></button><center>"; 
    html = "<tr><td>" + item.name + "</td><center><center><td> " + item.address + "</td></center><td><center>" + bttn_html + "</td></center>";
    return html;
}

$(function() {
    ajax_return("sites_list");
});


function edit(id, name, address){
    $('#modal-title').text(name);
    $('#modal_edit').modal('show');

    console.log(address)
    $('#edit_name').val(name);
    $('#edit_address').val(address);
    
}

function change(){

    //Pass the item id and the change as parameters the set_stock function if confirmed
    $(".change").attr("onclick","ajax_change('change_stock', {id: " + id + ", to_status: '" + to_status + "'});");  
    $('#modal_confirm').modal('show');
}

function add_site(){
    name = $('#add_name').val();
    address = $('#add_address').val();
    ajax_change("add_site", {"name": name, "address": address});
}