function saucOtro() {
    var teksts = document.getElementById('teksts').value;
    var dict = {txt: teksts};
    fetch('/otra', {
        method: 'POST',
        header: {'Content-Type': 'application/json'},
        body:JSON.stringify(dict)
    })
    .then(atb=>atb.json())
    .then(response=> {
        document.getElementById('pirma').style='display:none';        
        document.getElementById('otra').innerHTML=response.otra;
        otraLasa();        
    });    
}

function otraLasa() {
    fetch('/data/fails.json', {cache: "no-store"})
    .then(res => res.json())
    .then(data => otraRada(data));
}

function otraRada(dati) {
    console.log(dati.txt);
    document.getElementById('nolasiti').innerHTML=dati.txt;
}