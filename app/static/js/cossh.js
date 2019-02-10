function ajax_insert(item){
    html = "<tr><td>" + item.name + "</td><center><center><td> " + item.cossh + "</td></center>";
    return html;
}
$(function(){
    ajax_return("product_list");
});
