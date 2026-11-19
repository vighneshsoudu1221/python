document.getElementById("ac").addEventListener("click", clear);
document.getElementById("()").addEventListener("click", calculator);
document.getElementById("%").addEventListener("click", calculator);
document.getElementById("/").addEventListener("click", calculator);
document.getElementById("7").addEventListener("click", calculator);
document.getElementById("8").addEventListener("click", calculator);
document.getElementById("9").addEventListener("click", calculator);
document.getElementById("*").addEventListener("click", calculator);
document.getElementById("4").addEventListener("click", calculator);
document.getElementById("5").addEventListener("click", calculator);
document.getElementById("6").addEventListener("click", calculator);
document.getElementById("-").addEventListener("click", calculator);
document.getElementById("1").addEventListener("click", calculator);
document.getElementById("2").addEventListener("click", calculator);
document.getElementById("3").addEventListener("click", calculator);
document.getElementById("+").addEventListener("click", calculator);
document.getElementById("0").addEventListener("click", calculator);
document.getElementById(".").addEventListener("click", calculator);
document.getElementById("x").addEventListener("click", remove);
document.getElementById("=").addEventListener("click", calu);
let p_tag = document.querySelector("#display");
console.log(p_tag.innerText);
function calculator(event) {
  p_tag.value += event.target.innerText;
}
function clear() {
  p_tag.value = "";
}

function calu() {
  p_tag.value = eval(p_tag.value);
}

function remove() {
  p_tag.value = p_tag.value.slice(0, -1);
}
