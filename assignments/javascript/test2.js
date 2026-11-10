document.getElementById("b1").addEventListener("click", calucation);
document.getElementById("b2").addEventListener("click", calucation);
document.getElementById("b3").addEventListener("click", calucation);
document.getElementById("b4").addEventListener("click", calucation);
function calucation(event) {
  let v1, v2, res, p_tag;
  v1 = parseInt(document.getElementById("t1").value);
  v2 = parseInt(document.getElementById("t2").value);
  if (event.target.innerText == "add") {
    res = v1 + v2;
  } else if (event.target.innerText == "mul") {
    res = v1 * v2;
  } else if (event.target.innerText == "sub") {
    res = v1 - v2;
  } else {
    res = v1 / v2;
  }
  p_tag = document.getElementById("output");
  p_tag.innerText = res;
}

