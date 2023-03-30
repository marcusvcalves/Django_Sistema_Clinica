function mostrarSenha(){
    let pw = document.getElementById("userPassword");

    if(pw.type == "password"){
        pw.setAttribute("type", "text");
    }
    else if(pw.type == "text"){
        pw.setAttribute("type", "password");
    }
}