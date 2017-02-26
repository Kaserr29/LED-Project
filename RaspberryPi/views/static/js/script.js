  document.innerHTML = "test";
  alert("yolo");
  function test() {
    var n = document.getElementById("n").value;
    var c = document.getElementById("couleur");
    c.innerHTML = "";
    for (var i = 0; i < n; i++) {
      a =i+1;
      c.innerHTML += '<label for="c'+i+'">Couleur '+a+'</label><input type="color" name="c'+i+'" value="#ff0000">';
    }
  }
