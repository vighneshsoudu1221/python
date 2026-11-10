function display() {
  alert("lacuy");
}
function disk() {
  alert("fine");
}

function add() {
  let v1, v2, res, p_tag;
  v1 = parseInt(document.getElementById("t1").value);
  v2 = parseInt(document.getElementById("t2").value);
  res = v1 + v2;
  p_tag = document.getElementById("output");
  p_tag.innerText = res;
}

document.getElementById("b1").addEventListener("click", display);
document.getElementById("b2").addEventListener("click", display);
document.getElementById("b1").addEventListener("mouseover", changecolor);
function changecolor(event) {
  event.target.style.color = "red";
}
function display(event) {
  console.log(event);
}
