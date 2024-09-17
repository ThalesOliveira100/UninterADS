let botao = document.querySelector("#botao");
botao.style.background = "blue";
let estaQuebrado = false;
let contadorCliques = 0;

botao.addEventListener("mouseover", e => {
    if (!estaQuebrado) {
        botao.style.background = "green";
    }
});

botao.addEventListener("mouseout", e => {
    if (!estaQuebrado) {
        botao.style.background = "blue";
    }
})

botao.addEventListener("click", e => {
    contadorCliques++;

    if(contadorCliques >= 5) {
        botao.style.background = "red";
        botao.innerHTML = "Quebrei";
        estaQuebrado = true;
    }   
});

console.log(botao)