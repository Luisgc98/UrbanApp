function isNull(item){
    var value = item.value.trim();
    if((value.length == 0 || value.length < 3)
        || value == ""
        || value == undefined){
            return true;
        } else {
            return false;
        }
}

$(".text-field").on('input', function(){
    var p_text = this.parentNode.parentNode.lastElementChild;
    p_text.id = 'alert_'+this.id;
    p_text.textContent = 'El Nombre de Usuario debe tener 3 caracteres como mínimo';
    var value = this.value.trim();
    if(isNull(this) && this.value != ''){
        $("#alert_"+this.id).show(200);
        this.style.border = 'solid 1px red';
        p_text.style.color = '#571001';
    } else{
        $("#alert_"+this.id).hide(200);
        this.style.border = '';
        p_text.style.color = '';
    }
})

$(".psswd-field").on('input', function(){
    var p_text = this.parentNode.parentNode.lastElementChild;
    p_text.id = 'alert_'+this.id;
    var value = this.value.trim();
    var psswd = $(".psswd-c-field")[0];
    if(this.value != psswd.value && psswd.value != ''){
        p_text.textContent = 'Las contraseñas No coinciden';
    } else {
        p_text.textContent = 'La contraseña debe tener 6 caracteres como mínimo, una Mayúscula, una Minúscula y un Numero';
    }
    if((isNull(this) || !/^(?=\w*\d)(?=\w*[A-Z])\S{6,12}$/.test(value) || (this.value != psswd.value && psswd.value != '')) && this.value != ''){
        $("#alert_"+this.id).show(200);
        this.style.border = 'solid 1px red';
        p_text.style.color = '#571001';
    } else{
        $("#alert_"+this.id).hide(200);
        this.style.border = '';
        p_text.style.color = '';
    }
})

$(".psswd-c-field").on('input', function(){
    var p_text = this.parentNode.parentNode.lastElementChild;
    p_text.id = 'alert_'+this.id;
    var value = this.value.trim();
    var psswd = $(".psswd-field")[0];
    if(!/^(?=\w*\d)(?=\w*[A-Z])\S{6,12}$/.test(psswd.value)){
        p_text.textContent = 'La contraseña debe tener 6 caracteres como mínimo, una Mayúscula, una Minúscula y un Numero';
    } else {
        p_text.textContent = 'Las contraseñas No coinciden';
    }
    if((isNull(this) || (this.value != psswd.value && psswd.value != '') || !/^(?=\w*\d)(?=\w*[A-Z])\S{6,12}$/.test(psswd.value)) && (this.value != '' || this.value != psswd.value)){
        $("#alert_"+this.id).show(200);
        this.style.border = 'solid 1px red';
        p_text.style.color = '#571001';
    } else{
        $("#alert_"+this.id).hide(200);
        this.style.border = '';
        p_text.style.color = '';
    }
})

$(".email-field").on('input', function(){
    var p_text = this.parentNode.parentNode.lastElementChild;
    p_text.id = 'alert_'+this.id;
    var value = this.value.trim();
    p_text.textContent = 'Correo electrónico inválido';
    if((isNull(this) || !/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i.test(value)) && this.value != ''){
        $("#alert_"+this.id).show(200);
        this.style.border = 'solid 1px red';
        p_text.style.color = '#571001';
    } else{
        $("#alert_"+this.id).hide(200);
        this.style.border = '';
        p_text.style.color = '';
    }
})