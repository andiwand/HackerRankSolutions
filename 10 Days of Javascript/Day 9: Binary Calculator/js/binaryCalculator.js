function input(s) {
  document.getElementById("res").innerText += s;
}

function clearInput() {
  document.getElementById("res").innerText = "";
}

function calc() {
  const i = document.getElementById("res").innerText;

  const re = /^([01]+)([+\-*\/])([01]+)$/;
  const m = i.match(re);
  
  const a = Number.parseInt(m[1], 2);
  const b = Number.parseInt(m[3], 2);

  const c = eval(`${a}${m[2]}${b}`);

  document.getElementById("res").innerText = c.toString(2);
}