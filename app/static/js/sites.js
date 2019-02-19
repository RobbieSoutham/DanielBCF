function ajax_insert(item){
    btn1 = "<button type='button' class='buttons' id='edit' onclick='edit(" + item.id + ", \"" + item.name + "\", \"" + item.address + "\");'><img src='" + $SCRIPT_ROOT + "/static/open-iconic-master/svg/pencil.svg' alt='pencil'></button>"; 
    btn2 = "<button class='buttons' id='delete' onclick='delete_site(" + item.id + ");'><img src='" + $SCRIPT_ROOT + "/static/open-iconic-master/svg/x.svg' alt='x'></button>";
    html = "<tr><td class='name'>" + item.name + "</td><center><center><td> " + item.address + "</td></center><td><center>" + btn1 + btn2 + "</center></td>";
    return html;
}

$(function() {
    ajax_return("sites_list");
    $("#site_id").parent().css("display", "none");

});

function edit(id, name, address){
    //Change modal for editing a site, enter site_id to send to flask form
    $('#modal-title').text(name);
    $('#modal').modal('show');
    $("#site_id").parent().css("display", "block");
    $("#name").val("Edit");
    $("#site_id").val(id)
    $('#name').val(name);
    $('#address').val(address);
    
}
function reset_modal(){
    //Reset modal so values dont stick for adding a site
    $("#name").val("");
    $("#address").val("");
    $("#name").val("Add");
    $("#site_id").parent().css("display", "none");
    $("#site_id").val("");
    $("#modal-title").text("Add Site");
    $('#modal').modal('hide');
}

function delete_site(id){
    ajax_change("delete_site", {"id": id});
    load_content();
}

function load_content(){
    $("td").remove();
    ajax_return("sites_list");
}