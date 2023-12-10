function sumTable() {
    const prices = document.querySelectorAll("td:nth-child(2)"); 

    let sum = 0;

    for (let index = 0; index < prices.length; index++) {
        sum += Number(prices[index].textContent);
    }

    document.getElementById("sum").textContent = sum.toFixed(2);
}