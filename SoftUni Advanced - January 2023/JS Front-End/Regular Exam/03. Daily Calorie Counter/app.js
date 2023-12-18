window.addEventListener("load", solve);

function solve() {
    const loadMealsBtn = document.getElementById("load-meals");
    const addMealBtn = document.getElementById("add-meal");
    const editMealBtn = document.getElementById("edit-meal");
    const foodInput = document.getElementById("food");
    const timeInput = document.getElementById("time");
    const caloriesInput = document.getElementById("calories");
    const mealsList = document.getElementById("list");


    loadMealsBtn.addEventListener("click", loadMeals);
    addMealBtn.addEventListener("click", addMeal);
    editMealBtn.addEventListener("click", editMeal);



    //-----------------------------------------------------------------      LOAD
    function loadMeals() {
        fetch("http://localhost:3030/jsonstore/tasks")
            .then(response => response.json())
            .then(data => {
                mealsList.innerHTML = "";
                Object.entries(data).forEach(([key, meal]) => {
                    const mealDiv = createMealElement(meal);
                    mealsList.appendChild(mealDiv);
                });
            })
            .catch(error => console.error(error));
    }



    //----------------------------------------------------------          ADD/POST
    function addMeal() {
        const food = foodInput.value;
        const time = timeInput.value;
        const calories = caloriesInput.value;

        if (food === "" || time === "" || calories === "") {
            return;
        }

        const meal = { food, time, calories };

        fetch("http://localhost:3030/jsonstore/tasks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(meal)
        })
            .then(response => response.json())
            .then(() => {
                loadMeals();
                clearInputs();
            })
            .catch(error => console.error(error));
    }



    //---------------------------------------------------------------------           EDIT/PUT
    function editMeal() {
        const selectedMeal = document.querySelector(".selected");


        if (!selectedMeal) {
            return;
        }


        const id = selectedMeal.dataset.id;
        const food = foodInput.value;
        const time = timeInput.value;
        const calories = caloriesInput.value;


        if (food === "" || time === "" || calories === "") {
            return;
        }


        const meal = { food, time, calories };


        fetch(`http://localhost:3030/jsonstore/tasks/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(meal)
        })
            .then(response => response.json())
            .then(() => {
                loadMeals();
                clearInputs();
                enableAddMealButton();
            })
            .catch(error => console.error(error));
    }



    //---------------------------------------------------------------------------------      CREATE
    function createMealElement(meal) {
        const mealDiv = document.createElement("div");
        mealDiv.classList.add("meal");
        mealDiv.dataset.id = meal._id;


        mealDiv.innerHTML = `
            <h2>${meal.food}</h2>
            <h3>${meal.time}</h3>
            <h3>${meal.calories}</h3>
            <div id="meal-buttons">
                <button class="change-meal">Change</button>
                <button class="delete-meal">Delete</button>
            </div>
        `;


        const changeBtn = mealDiv.querySelector(".change-meal");
        const deleteBtn = mealDiv.querySelector(".delete-meal");


        changeBtn.addEventListener("click", () => {
            populateForm(meal);
            disableAddMealButton();
            selectMeal(mealDiv);
        });


        deleteBtn.addEventListener("click", () => deleteMeal(meal._id));


        return mealDiv;
    }



    function populateForm(meal) {
        foodInput.value = meal.food;
        timeInput.value = meal.time;
        caloriesInput.value = meal.calories;
    }



    //------------------------------------------------------------------------          DELETE/DELETE
    function deleteMeal(id) {
        fetch(`http://localhost:3030/jsonstore/tasks/${id}`, {
            method: "DELETE"
        })
            .then(() => {
                loadMeals();
                clearInputs();
                enableAddMealButton();
            })
            .catch(error => console.error(error));
    }



    function selectMeal(mealDiv) {
        const selectedMeal = document.querySelector(".selected");
        if (selectedMeal) {
            selectedMeal.classList.remove("selected");
        }

        mealDiv.classList.add("selected");
    }




    function disableAddMealButton() {
        addMealBtn.disabled = true;
        editMealBtn.disabled = false;
    }
    function enableAddMealButton() {
        addMealBtn.disabled = false;
        editMealBtn.disabled = true;
    }




    function clearInputs() {
        foodInput.value = "";
        timeInput.value = "";
        caloriesInput.value = "";
    }
}