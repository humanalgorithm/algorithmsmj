function sortsubmit(sortname, csrf_token) {
    var url = sortname + "/";
    //csrf_token = "{{ csrf_token }}";
    var arraysize = 90;
    $('#div3').text(document.getElementById('div2').innerHTML);
    var array = createArray();
    var timeout = 30000

    $("#time").text("");
    $("#time").append("<img id='time' src='/static/css/ajax-loader.gif'/>");
    $.ajax({
        type: "POST",
        url: url,
        data: {
            array: JSON.stringify(array),
            csrfmiddlewaretoken: csrf_token
        },

        success: function (data) {
            var getData = JSON.parse(data);

            if (getData.error != "timeout") {
                $('#div2').text(getData.array);
                var shortarray = shortenArray(arraysize);
                if (shortarray.length >= arraysize) {
                    $('#div1').text(shortarray + "...");
                }
                else {
                    $('#div1').text(shortarray);
                }
                $('#div1').css({"font-size": "20px"});


                $('#time').text("Time to execute: " + getData.time);
                $('#time').css({"font-size": "20px"});
            }
            else {
                $('#time').text("There was a timeout error after " + getData.time + " seconds. Please try a shorter array");
                $('#time').css({"font-size": "20px"});
            }
        },
        error: function (data) {
            $('#time').text("Array too large, please enter a shorter array");
            $('#time').css({"font-size": "20px"});
        }


    });

    return false;
}
