function initMap(x,y) {
    var latCoord = parseFloat(x);
    var lngCoord = parseFloat(y);
    var coords = {lat: latCoord, lng: lngCoord};
    var map = new google.maps.Map(document.getElementById('map'), 
    {
      zoom: 12,
      center: coords
    });
    return map;
}

function addMarker(mainMap){
    var myLatLng = {lat: 33.6857, lng: -117.8259};
    var marker = new google.maps.Marker({
        position: myLatLng,
        map: mainMap
    });
    return marker;
}

function dropDownList(){
    var select = document.getElementById('dropdown');
    var newOptions = ['Irvine', 'West Covina', 'Los Angeles'];
    for(var i = 0; i < newOptions.length; i++)
    {
        var option = document.createElement("option");
        option.text = newOptions[i];
        option.value = newOptions[i];
        select.appendChild(option);
    }
}

function test()
{
    $.ajax({
        type: "POST",
        url: '/getData',
        data: data,
        success: test2(result)
    });
}

function test2(data){
    alert(data);
}