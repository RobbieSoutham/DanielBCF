function ajax_insert(item){
    html = "<tr><td>" + item.name + "</td><center><center><td><a href='" + item.cossh + "'>" + item.cossh + "</a></td></center>";
    return html;
}

function ajax_follow(){
}

$(function(){
    ajax_return("product_list");
});
