document.getElementById("b1").addEventListener("click", calcucation);
document.getElementById("b2").addEventListener("click", calcucation);
document.getElementById("b3").addEventListener("click", calcucation);
let value = 0;
function calcucation(event) {
let  p_tag;
  if (event.target.innerText == "increment") {
    value = value + 1;
  } else if (event.target.innerText == "decrement") {
    value = value - 1;
  } else if (event.target.innerText == "restart") {
    value = 0;
  }
  p_tag = document.getElementById("outin");
  p_tag.innerText = value;
}
