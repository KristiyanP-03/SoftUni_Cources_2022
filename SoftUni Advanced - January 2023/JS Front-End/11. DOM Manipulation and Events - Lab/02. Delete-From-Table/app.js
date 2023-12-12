function deleteByEmail() {
    let targetEmailToDelete = document.querySelector("input").value;
    let arrayOfEmails = document.querySelectorAll("tbody tr");

    arrayOfEmails.forEach(tr => {
        let email = tr.cells[1];

        if (email.textContent === targetEmailToDelete) {
            tr.parentNode.removeChild(tr);
        }
    });


    document.querySelector("input").value = "";
}