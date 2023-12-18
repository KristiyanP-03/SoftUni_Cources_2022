window.addEventListener("load", solve);

function solve() {

    const addingInfoBtn = document.getElementById("add-btn");
    const previewList = document.getElementById("preview-list");
    const expensesList = document.getElementById("expenses-list");
    const deleteBtn = document.querySelector(".delete");
  

    addingInfoBtn.addEventListener("click", addButtonClick);
    deleteBtn.addEventListener("click", deleteButtonClick);



    let expenseType = "";
    let amount = "";
    let date = "";
  

    //------------------------------------------------------------------------     Add
    function addButtonClick() {
        const expenseInput = document.getElementById("expense");
        const amountInput = document.getElementById("amount");
        const dateInput = document.getElementById("date");

  
        expenseType = expenseInput.value;
        amount = amountInput.value;
        date = dateInput.value;

  


        if (expenseType == "" || amount == "" || date == "") {
            return;
        }
  


        const li = document.createElement("li");
        li.classList.add("expense-item");

      
        const article = document.createElement("article");
  

        const pForType = document.createElement("p");
        pForType.textContent = `Type: ${expenseType}`;
  

        const pForAmount = document.createElement("p");
        pForAmount.textContent = `Amount: ${amount}$`;
  

        const pForDate = document.createElement("p");
        pForDate.textContent = `Date: ${date}`;
  


        article.appendChild(pForType);
        article.appendChild(pForAmount);
        article.appendChild(pForDate);
  


        //------------------------------------------------------------------             Edit btn
        const buttonsDiv = document.createElement("div");
        buttonsDiv.classList.add("buttons");
  
        const editBtn = document.createElement("button");
        editBtn.classList.add("btn", "edit");
        editBtn.textContent = "edit";
        editBtn.addEventListener("click", () => editButtonClick(li, expenseType, amount, date));



        //----------------------------------------------------------------------------      OK btn
        const okBtn = document.createElement("button");
        okBtn.classList.add("btn", "ok");
        okBtn.textContent = "ok";
        okBtn.addEventListener("click", () => okButtonClick(li, expenseType, amount, date));
  


        buttonsDiv.appendChild(editBtn);
        buttonsDiv.appendChild(okBtn);
  
        li.appendChild(article);
        li.appendChild(buttonsDiv);
  
        previewList.appendChild(li);
  


        //!!! resets
        addingInfoBtn.disabled = true;
        expenseInput.value = "";
        amountInput.value = "";
        dateInput.value = "";
    }
  


    //--------------------------------------------------------------------    Edit
    function editButtonClick(li, expenseType, amount, date) {
        addingInfoBtn.disabled = false;
  
        previewList.removeChild(li);
  
        document.getElementById("expense").value = expenseType;
        document.getElementById("amount").value = amount;
        document.getElementById("date").value = date;
    }
  


    //----------------------------------------------------------------------   OK
    function okButtonClick(li, expenseType, amount, date) {
        addingInfoBtn.disabled = false;

        if (expenseType == "" || amount == "" || date == "") {
            return;
        }
        
      
        const updatedLi = document.createElement("li");
        updatedLi.classList.add("expense-item");
      
        const article = document.createElement("article");
      
        const pForType = document.createElement("p");
        pForType.textContent = `Type: ${expenseType}`;
      
        const pForAmount = document.createElement("p");
        pForAmount.textContent = `Amount: ${amount}$`;
      
        const pForDate = document.createElement("p");
        pForDate.textContent = `Date: ${date}`;
      
        article.appendChild(pForType);
        article.appendChild(pForAmount);
        article.appendChild(pForDate);
      
        updatedLi.appendChild(article);
      
        previewList.removeChild(li);
      
        expensesList.appendChild(updatedLi);
      }
  



    //----------------------------------------------------------------------    Delete
    function deleteButtonClick() {
        location.reload();
    }
}