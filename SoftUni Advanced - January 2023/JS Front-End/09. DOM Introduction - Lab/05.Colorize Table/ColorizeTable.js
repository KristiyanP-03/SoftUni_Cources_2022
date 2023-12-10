function colorize() {
    const allRows = Array.from(document.querySelectorAll('td'));

    for (let index = 0; index < allRows.length; index += 4) {
        allRows[index].style.background = 'teal';
        allRows[index + 1].style.background = 'teal';
    }
}