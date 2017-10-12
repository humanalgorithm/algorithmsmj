
function resetDataset() {
    div_id_from = "#dataset_submit"
    div_id_to = "#dataset_display"
    setDatasetDisplay(div_id_from, div_id_to)
    $('#time_display').text("Time to Execute\:");
}

function setDatasetDisplay(div_id_from, div_id_to) {
    max_array_display_size = 150

    from_div_text = $(div_id_from).text()
    from_div_array = from_div_text.split(',');
    from_div_array_length = from_div_array.length
    if (from_div_array_length > max_array_display_size) {
        truncated_array = from_div_array.slice(0, max_array_display_size)
        $(div_id_to).text(truncated_array + "...");
    }
    else {
        $(div_id_to).text(from_div_text)
    }
}