$("#remember_me").change(function() {
    if(this.checked) {
        $("#remember_me").value("")
    }
    else{
      $("#remember_me").value("1")
    }
});
