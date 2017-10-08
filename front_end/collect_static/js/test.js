function shortenArray(arrayin) {
    arrayLength = 30;
    var temp = new Array();
    temp = arrayin.split(',');
    i = 0;
    while (i < arrayLength) {
        temp[i] = parseInt(temp[a], 10);
        if (i == temp.length) {
            break;
        }
        i++;
    }

    if (i >= arrayLength - 1) {
        temp[i] = ".";
        temp[i + 1] = ".";
        temp[i + 2] = "."

    }

    return temp
}