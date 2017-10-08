
function resetarray() {
    var arraysize = 90;
    var lastarray = document.getElementById('div3').innerHTML

    if (lastarray.length == 0) {
    }
    else {
        $('#div2').text(lastarray);
        var shortarray = shortenArray(arraysize)

        if (shortarray.length >= arraysize) {
            $('#div1').text(shortarray + "...");
        }
        else {
            $('#div1').text(shortarray);
        }

        $('#time').text("Time to Execute\:");
    }

}


function shortenArray(arrayLength) {
    var temp = new Array();
    htmlContent = document.getElementById('div2').innerHTML;
    var newarray = new Array();

    temp = htmlContent.split(',');
    var i = 0;

    for (a in temp) {
        newarray[a] = parseInt(temp[a], 10);
        if (a >= arrayLength - 1) {
            break;
        }
    }
    return newarray;
}