
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf8">
    <title>LEDControl</title>
  </head>
    <body>
    <form action="/LEDControl" method="post">

      <label for="h">Durée Allumé</label>
      <input type="range" name="h" id="h" value="1000" min="0" max="1000" oninput="ho.value = h.value">
      <input type="number" name="ho" id="ho" value="1000" min="0" max="1000" oninput="h.value = ho.value"/>

      <label for="h">Durée Transition</label>
      <input type="range" name="t" id="t" value="0" min="0" max="1000" oninput="to.value = t.value">
      <input type="number" name="to" id="to" value="0"min="0" max="1000" oninput="t.value = to.value"/>

      <label for="n">Nombre de couleurs</label>
      <select id="n" name="n" oninput="" onchange="test()">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
        <option value="10">10</option>
      </select>

      <br/>
      <br/>
      <br/>

      <div id="couleur">
        <label for="c0">Couleur 1</label>
        <input type="color" id="c0" name="c0" onchange="br()">
      </div>

      <br/>
      <br/>
      <br/>

      <input value="Valider" type="submit"/>
  </body>
      <script src="static/script.js"></script>
</html>
