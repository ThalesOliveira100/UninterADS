const campo1 = document.querySelector("#campo1");
const campo2 = document.querySelector("#campo2");
const seletor = document.querySelector("#operacao");
let resposta = document.querySelector("#resposta");

seletor.addEventListener("change", calcular);
campo1.addEventListener("keyup", calcular);
campo2.addEventListener("keyup", calcular);

function calcular() {
    if (campo1.value != "" && campo2.value != "") {
        const valor1 = parseInt(campo1.value);
        const valor2 = parseInt(campo2.value);

        const operacao = seletor.value;
        
        if (operacao === "somar")
            resposta.innerHTML = valor1 + valor2;
        
        if (operacao === "subtrair")
            resposta.innerHTML = valor1 - valor2;

        if (operacao === "multiplicar")
            resposta.innerHTML = valor1 * valor2;

        if (operacao === "dividir")
            resposta.innerHTML = valor1 / valor2;
    }
}