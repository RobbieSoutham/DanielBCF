function ajax_insert(item){
    var btn1 = "<button type='button' class='buttons' id='edit' onclick='edit(\"" + item.name + "\", \"" + item.address + "\");'><img src='" + $SCRIPT_ROOT + "/static/open-iconic-master/svg/pencil.svg' alt='pencil'></button>"; 
    var btn2 = "<button class='buttons' id='delete' onclick='delete_site(\"" + item.name + "\");'><img src='" + $SCRIPT_ROOT + "/static/open-iconic-master/svg/x.svg' alt='x'></button>";
    var html = "<tr><td class='name'>" + item.name + "</td><center><center><td> " + item.address + "</td></center><td><center>" + btn1 + btn2 + "</center></td>";
    return html;
}

$(function() {
    ajax_return("sites_list");
    $("#site_id").parent().css("display", "none");
    $("#edit").parent().css("display", "none");
    $("#previous_name").parent().css("display", "none");

});

function edit(name, address){
    //Change modal for editing a site, enter site_id to send to flask form
    $("#previous_name").val(name);
    $("#modal-title").text(name);
    $("#modal").modal("show");
    $("input[type='checkbox']").prop("checked", true);
    $("#name").val(name);
    $("#address").val(address);
    
}
function reset_modal(){
    //Reset modal so values dont stick for adding a site
    $("input[type='checkbox']").prop("checked", false);
    $("#name").val("");
    $("#address").val("");
    $("#name").val("");
    $("#modal-title").text("Add Site");
    $("#modal").modal("hide");
}

function delete_site(name){
    ajax_change("delete_site", {"name": "'" + name + "'"});
}

function load_content(){
    $("td").remove();
    ajax_return("sites_list");
}

function ajax_follow(){
}
