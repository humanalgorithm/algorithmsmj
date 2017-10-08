var ExecuteSortService = {
    executeSort: function (sort_name) {
        $('#div3').text(document.getElementById('div2').innerHTML);
        var current_dataset = this._getCurrentDataset();
        this._setLoadingImg()
        this._makeAjaxRequest(sort_name, current_dataset)
    },
    _getCsrfToken: function () {
        return document.getElementById('token').getElementsByTagName("input")[0].value
    },
    _setLoadingImg: function () {
        $("#time").text("");
        $("#time").append("<img id='time' src='/static/css/ajax-loader.gif'/>");
    },
    _getCurrentDataset: function () {
        var node = document.getElementById('div2')
        htmlContent = node.innerHTML
        var return_dataset = []
        html_elements = htmlContent.split(',');
        for (var i = 0; i < html_elements.length; i++) {
            return_dataset.push(parseInt(html_elements[i], 10));
        }
        return return_dataset
    },
    _makeAjaxRequest: function (sort_name, current_dataset) {
        var url = sort_name + "/";
        csrf_token  = this._getCsrfToken()
        self = this
        $.ajax({
            type: "POST",
            url: url,
            dataType: "json",
            traditional: true,
            data: {
                dataset: current_dataset,
                csrfmiddlewaretoken: csrf_token
            },
            success: function(response_data) {
                //var response_content = JSON.parse(response_data);
                if (response_data.error != "timeout") {
                    self._setSortedResult(response_data)
                }
                else {
                    self._setTimeoutError(response_data)
                }
            },
            error: function (data) {
                self._setTooLargeDatasetError()
            }
        });

        return false;
    },
    _setTimeoutError: function (response_content) {
        $('#time').text("There was a timeout error after " + response_content.time + " seconds. Please try a shorter array");
        $('#time').css({"font-size": "20px"});
    },
    _setTooLargeDatasetError: function () {
        $('#time').text("Array too large, please enter a shorter array");
        $('#time').css({"font-size": "20px"});
    },

    _setSortedResult: function (response_content) {
        $('#div2').text(response_content.sorted_dataset);
        var shortarray = shortenArray(arraysize);
        if (shortarray.length >= arraysize) {
            $('#div1').text(shortarray + "...");
        }
        else {
            $('#div1').text(shortarray);
        }
        $('#div1').css({"font-size": "20px"});


        $('#time').text("Time to execute: " + time);
        $('#time').css({"font-size": "20px"});
    }
}


