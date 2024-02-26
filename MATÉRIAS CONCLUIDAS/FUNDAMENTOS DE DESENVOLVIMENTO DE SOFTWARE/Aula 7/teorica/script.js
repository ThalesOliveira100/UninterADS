console.log('日本語で書いても大丈夫。')

const paragrafo = document.querySelector("#para1");

paragrafo.addEventListener("mouseover", mudaVerde);
paragrafo.addEventListener("mouseout", mudaVermelho);

function mudaVerde() {
    paragrafo.style.background = "green";
}

function mudaVermelho() {
    paragrafo.style.background = "red";
}