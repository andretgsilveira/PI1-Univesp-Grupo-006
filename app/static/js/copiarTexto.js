function copiarTexto() {
    var textoCopiado = document.getElementById("link");
    textoCopiado.select();
    document.execCommand("Copy");
    alert("Chave Pix Copiada: " + textoCopiado.value);
}