var GetRandomDatasetService = {
    getRandom: function () {
        csrf_token = this._getCsrfToken()
        var user_array_size = document.getElementById('user_array_size').value;
        if (this._validInt(user_array_size)) {
            this._setLoadingImg()
            this._ajaxRequestRandomDataset(user_array_size, csrf_token)
        }
        else {
            this._setInvalidInputMsg()
        }
    },
    _setLoadingImg: function () {
        $("#time_display").text("");
        $("#time_display").append("<img id='time' src='/static/img/ajax-loader.gif'/>");
    },
    _getCsrfToken: function () {
        return document.getElementById('token').getElementsByTagName("input")[0].value
    },
    _validInt: function (dataset_size) {
        return (dataset_size == parseInt(dataset_size, 10) && dataset_size != 0)
    },
    _ajaxRequestRandomDataset: function (user_array_size, csrf_token) {
        var url = "/get_random_dataset/";
        var self = this
        $.ajax({
            type: "POST",
            url: url,
            data: {dataset_size: user_array_size, csrfmiddlewaretoken: csrf_token},
            success: function (response_data) {
                self._setRandomDataResult(response_data)
                self._setSuccessMsg()
            },
            error: function (response_data) {
                self._setErrorMsg(response_data)
            }
        });

        return false;
    },
    _setRandomDataResult: function(response_data) {
        div_id_from = '#dataset_submit'
        div_id_to = '#dataset_display'
        $(div_id_from).text(response_data);
        setDatasetDisplay(div_id_from, div_id_to)
    },
    _setSuccessMsg: function () {
        $('#dataset_display').css({"font-size": "20px"});
        $('#time_display').text("Success");
    },
    _setErrorMsg: function (response_data) {
        error_msg = JSON.parse(response_data.responseText).error
        $('#time_display').text(error_msg);
        $('#time_display').css({"font-size": "20px"});
    },
    _setInvalidInputMsg: function () {
        $("#time_display").text("Please enter an integer for array size");
    }
}