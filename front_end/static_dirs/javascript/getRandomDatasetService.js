var GetRandomDatasetService = {
    getRandom: function () {
        $('#div3').text(document.getElementById('div2').innerHTML)
        csrf_token = this._getCsrfToken()
        var dataset_size = document.getElementById('arraysize').value;
        if (this._validInt(dataset_size)) {
            this._setLoadingImg()
            this._ajaxRequestRandomDataset(dataset_size, csrf_token)
        }
        else {
            this._setInvalidInputMsg()
        }
    },

    _setLoadingImg: function () {
        $("#time").text("");
        $("#time").append("<img id='time' src='/static/css/ajax-loader.gif'/>");
    },

    _getCsrfToken: function () {
        return document.getElementById('token').getElementsByTagName("input")[0].value
    },

    _validInt: function (dataset_size) {
        return (dataset_size == parseInt(dataset_size, 10) && dataset_size != 0)
    },

    _ajaxRequestRandomDataset: function (arraysizeselect, csrf_token) {
        var url = "/get_random_dataset/";
        var self = this
        $.ajax({
            type: "POST",
            url: url,
            data: {dataset_size: arraysizeselect, csrfmiddlewaretoken: csrf_token},
            success: function (data) {
                self._setDatasetText(data, arraysizeselect)
                self._setSuccessMsg()
            },
            error: function (data) {
                self._setErrorMsg(data)
            }
        });

        return false;
    },
    _setDatasetText: function (data, arraysize) {
        div_id = '#div2'
        $(div_id).text(data);
        var shortarray = shortenArray(arraysize);
        if (shortarray.length >= arraysize) {
            $('#div1').text(shortarray + "...");
        }
        else {
            $('#div1').text(shortarray);
        }
    },
    _setSuccessMsg: function () {
        $('#div1').css({"font-size": "20px"});
        $('#time').text("Success");
    },
    _setErrorMsg: function (data) {
        error_msg = JSON.parse(data.responseText).error
        $('#time').text(error_msg);
        $('#time').css({"font-size": "20px"});
    },
    _setInvalidInputMsg: function () {
        $("#time").text("Please enter an integer for array size");
    }
}