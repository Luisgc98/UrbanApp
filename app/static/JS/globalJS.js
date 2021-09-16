function clearItems(items){
    for(var i=0; i<items.length; i++){
        items[i].value = '';
        items[i].style.border = '';
    }
}

function hideItems(items){
    for(var i=0; i<items.length; i++){
        $("#"+items[i].id).hide(200);
        items[i].style.border = '';
    }
}