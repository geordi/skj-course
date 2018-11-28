var xmlhttp;

function showResult( str ) {
  if ( !str ) {
    document.getElementById( "livesearch" ).innerHTML = "";
    document.getElementById( "livesearch" ).style.border = "0px";
    return;
  }
  else {
    xmlhttp = GetXmlHttpObject();
    if ( xmlhttp == null ) {
      alert( "No XML HTTP Request" );
      return;
    }
    var url = "/livesearch";
    url = url + "/" + str;
    url = url + "/" + Math.random();
    xmlhttp.onreadystatechange = stateChanged;
    xmlhttp.open( "GET", url, true );
    xmlhttp.send( null );
  }
}

function stateChanged() {
  if ( xmlhttp.readyState == 4 ) {
    document.getElementById( "livesearch" ).innerHTML = xmlhttp.responseText;
    document.getElementById( "livesearch" ).style.border = "1px solid #A5ACB2";
  }
}

function GetXmlHttpObject() {
  if ( window.XMLHttpRequest ) {
    return new XMLHttpRequest();
  }
  
  if ( window.ActiveXObject ) {
    return new ActiveXObject( "Microsoft.XMLHTTP" );
  }

  return null;
}
