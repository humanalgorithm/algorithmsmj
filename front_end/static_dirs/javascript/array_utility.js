

function createArray()
{
   var node = document.getElementById('div2')

   htmlContent = node.innerHTML

   var temp = new Array();
   temp = htmlContent.split(',');
   for (a in temp ) {
   temp[a] = parseInt(temp[a], 10);
   }

 return temp
}

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

function getrandom() {
    var url = "/choosesort/";
    var arraysize = 90;
    $('#div3').text(document.getElementById('div2').innerHTML)
    csrf_token = document.getElementById('token').getElementsByTagName("input")[0].value;
    var arraysizeselect = document.getElementById('arraysize').value;
    if (arraysizeselect == parseInt(arraysizeselect, 10) && arraysizeselect != 0) {
        $("#time").text("");
        $("#time").append("<img id='time' src='/static/css/ajax-loader.gif'/>");
        $.ajax({
            type: "POST",
            url: url,
            data: {arraysize: arraysizeselect, csrfmiddlewaretoken: csrf_token},
            success: function (data) {

                $('#div2').text(data);
                var shortarray = shortenArray(arraysize);
                if (shortarray.length >= arraysize) {
                    $('#div1').text(shortarray + "...");
                }
                else {
                    $('#div1').text(shortarray);
                }

                $('#div1').css({"font-size": "20px"});
                $('#time').text("Time to Execute\:");
            },
            error: function (data) {
                //window.alert("in error");
                $('#time').text("Array too big: please enter a shorter array size");
                $('#time').css({"font-size": "20px"});
            }
        });

        return false; // avoid to execute the actual submit of the form.
    }
    else {
        $("#time").text("Please enter an integer for array size");
    }
}

function shortenArray(arrayLength) { //window.alert("in shorten");
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