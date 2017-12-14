var xmlhttp;

function showResult( ) {
    xmlhttp = GetXmlHttpObject();
    if ( xmlhttp == null ) {
        alert( "Your browser does not support XML HTTP Request" );
        return;
    }
    var url = "/points";
    xmlhttp.onreadystatechange = stateChanged;
    xmlhttp.open( "GET", url, true );
    xmlhttp.send( null );
}

function stateChanged() {
    console.log('rt:', xmlhttp.responseText);
    console.log('len:', xmlhttp.responseText.length);
    if ( xmlhttp.responseText.length > 0 ) {
        var points_in_json = JSON.parse(xmlhttp.responseText);
        console.log('points_in_js:', points_in_json);
        for ( var p in points_in_json ) {
            console.log( 'point:', points_in_json[ p ] );
            addPoint( points_in_json[ p ] );
        }
    }
}

function GetXmlHttpObject() {
    if ( window.XMLHttpRequest ) {
        // code for IE7+, Firefox, Chrome, Opera, Safari
        return new XMLHttpRequest();
    }
    if ( window.ActiveXObject ) {
        // code for IE6, IE5
        return new ActiveXObject( "Microsoft.XMLHTTP" );
    }
    return null;
}
