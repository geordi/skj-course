var xmlhttp;

function showResult( str ) {
    if ( str.length == 0 ) {
        document.getElementById( "livesearch" ).innerHTML = "";
        document.getElementById( "livesearch" ).style.border = "0px";
        return;
    }

    xmlhttp = new XMLHttpRequest();

    let url = "/livesearch";
    url += "/"  + str;
    url += "/" + Math.random();

    xmlhttp.onreadystatechange = stateChange;
    xmlhttp.open( "GET", url, true );
    xmlhttp.send( null );
}

function stateChange() {
    if ( xmlhttp.readyState == 4 ) {
        document.getElementById( "livesearch" ).innerHTML = xmlhttp.responseText;
        document.getElementById( "livesearch" ).style.border = "1px solid #A5ACB2";
    }
}
