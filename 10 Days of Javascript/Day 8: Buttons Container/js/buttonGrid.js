function rotate() {
  const ids = ["btn4", "btn7", "btn8", "btn9", "btn6", "btn3", "btn2", "btn1"];
  
  const pre = ids.map(id => document.getElementById(id).textContent);
  
  for (let i = 0; i < pre.length; ++i) {
      document.getElementById(ids[i]).textContent = pre[(i+1)%8];
  }
}
