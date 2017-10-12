var ExecuteSortService = {
    executeSort: function (sort_name) {
        var current_dataset = this._getCurrentDataset();
        if (typeof(current_dataset) == 'undefined') {
            this._setDatasetError({"error": "Please select a dataset first"})
            return
        }
            this._setLoadingImg()
            this._makeAjaxRequest(sort_name, current_dataset)
    },
    _getCsrfToken: function () {
        return document.getElementById('token').getElementsByTagName("input")[0].value
    },
    _setLoadingImg: function () {
        $("#time_display").text("");
        $("#time_display").append("<img id='time' src='/static/img/ajax-loader.gif'/>");
    },
    _getCurrentDataset: function () {
        var dataset_submit_element = $("#dataset_submit")
        html_content = dataset_submit_element.text()
        var return_dataset = []
        html_elements = html_content.split(',');
        for (var i = 0; i < html_elements.length; i++) {
            return_dataset.push(parseInt(html_elements[i], 10));
        }
        if (html_elements[0] == ""){return}
        return return_dataset
    },
    _makeAjaxRequest: function (sort_name, current_dataset) {
        var url = "/get_sort_result/";
        csrf_token = this._getCsrfToken()
        self = this
        $.ajax({
            type: "POST",
            url: url,
            dataType: "json",
            traditional: true,
            data: {
                dataset: current_dataset,
                csrfmiddlewaretoken: csrf_token,
                sort_name: sort_name
            },
            success: function (response_data) {
                if (response_data.error != "timeout") {
                    self._setSortedResult(response_data)
                }
                else {
                    self._setTimeoutError(response_data)
                }
            },
            error: function (response_data) {
                self._setDatasetError(response_data)
            }
        });

        return false;
    },
    _setTimeoutError: function (response_data) {
        $('#time_display').text("There was a timeout error after " + response_data.time + " seconds. Please try a shorter array");
        $('#time_display').css({"font-size": "20px"});
    },
    _setDatasetError: function (response_data) {
        error_msg = response_data.error
        $('#time_display').text(error_msg);
        $('#time_display').css({"font-size": "20px"});
    },
    _setSortedResult: function (response_data) {
        div_id_from = '#dataset_received'
        div_id_to = '#dataset_display'
        $(div_id_from).text(response_data.sorted_dataset);
        setDatasetDisplay(div_id_from, div_id_to)

        $('#dataset_display').css({"font-size": "20px"});
        $('#time_display').text("Time to execute: " + response_data.time);
        $('#time_display').css({"font-size": "20px"});
    }
}


