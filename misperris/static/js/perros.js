function valida(){
var name, raza, descrip
name = document.getElementById("txtNombre").value;
raza = document.getElementById("txtRaza").value;
descrip = document.getElementById("txtDescripcion").value;

if (name.split('').length < 2) {
    alert("Ingrese nombre valido");
    return false;
}else if (raza.split('').length <2){
    alert("Ingrese una raza valida");
    return false;
}else if (descrip.length < 5)
{
    alert("Ingrese una descripción mas larga");
    return false;
}
}