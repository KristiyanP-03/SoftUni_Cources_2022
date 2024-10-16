function composedObjectBreakDown(array: string[]) {
    let outputArray: (string | number)[] = [];


    for (let index = 0; index < array.length; index++) {
        const element: string | number = array[index];
        
        if (index % 2 === 1) {
            outputArray.push(parseInt(element));
        }
        else{
            outputArray.push(element);
        }
    }

    console.log(outputArray);
};

const testArrayCase: string[] = ['Yoghurt', '48', 'Rise', '138', 'Apple', '52'];

composedObjectBreakDown(testArrayCase);