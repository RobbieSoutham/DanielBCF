$("#remember_me").change(function() {
    if(this.checked) {
        $("#remember_me").val("")
    }
    else{
      $("#remember_me").val("1")
    }
});
