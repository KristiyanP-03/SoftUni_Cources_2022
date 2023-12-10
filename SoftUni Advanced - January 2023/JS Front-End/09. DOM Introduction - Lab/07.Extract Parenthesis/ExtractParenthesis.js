function extract(elementId) {
    const targetElement = document.getElementById(elementId);

    if (targetElement) {
        const text = targetElement.textContent;
        const regex = /\(([^)]+)\)/g;
        const matches = text.match(regex);

        if (matches) {
            const result = matches.map(match => match.slice(1, -1)).join('; ');
            console.log(result);
            return result;
        } else {
            console.log("No matches found");
            return "";
        }
    } else {
        console.log("Element not found");
        return "";
    }
}