function kalkulal(){
    const width=document.getElementById('szelesseg').value;
    const height=document.getElementById('magassag').value;
    const paper=document.getElementById('papirtipus').value;

    let area=Math.round((width*height)/10000);    
    let cost=area*paper;

    document.getElementById('terulet').innerHTML = area;
    document.getElementById('papir').innerHTML = paper;
    document.getElementById('koltseg').innerHTML = cost;
    document.getElementById('valasz').style.visibility = "visible";
}

