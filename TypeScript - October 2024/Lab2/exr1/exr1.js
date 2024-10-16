function composedObjectBreakDown(array) {
    var outputArray = [];
    for (var index = 0; index < array.length; index++) {
        var element = array[index];
        if (index % 2 === 1) {
            outputArray.push(parseInt(element));
        }
        else {
            outputArray.push(element);
        }
    }
    console.log(outputArray);
}
;
var testArrayCase = ['Yoghurt', '48', 'Rise', '138', 'Apple', '52'];
composedObjectBreakDown(testArrayCase);
