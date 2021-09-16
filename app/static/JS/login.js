$(".btn-tabs").on('click', function(){
    //this.style.display = 'none';
    $("#"+this.id).hide();
    if(this.name=="register_tab"){
        $("#title_header")[0].textContent="Regístrate";
        $("#login_tab").show(200);
    } else{
        $("#title_header")[0].textContent="Inicia Sesión";
        $("#register_tab").show(200);
    }
    clearItems($(".field"));
    hideItems($(".alert-text"));
})