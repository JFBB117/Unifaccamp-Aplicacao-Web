const botao = document.getElementById("botao");
const nome = document.getElementById("nome");
const mensagem = document.getElementById("mensagem");

botao.addEventListener("click", async function () {
    const resposta = await fetch("/api/hello");
    const dados = await resposta.json();
    mensagem.textContent = dados.mensagem + " " + nome.value;
});