window.addEventListener("load", solve);

function solve() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
    const locationInput = document.getElementById('location');
    const temperatureInput = document.getElementById('temperature');
    const dateInput = document.getElementById('date');
    const addWeatherBtn = document.getElementById('add-weather');
    const editWeatherBtn = document.getElementById('edit-weather');
    const loadHistoryBtn = document.getElementById('load-history');
    const listContainer = document.getElementById('list');

    loadHistoryBtn.addEventListener('click', loadHistoryHandler);
    addWeatherBtn.addEventListener('click', addWeatherHandler);
    editWeatherBtn.addEventListener('click', editWeatherHandler);

    async function loadHistoryHandler() {
        try {
            const response = await fetch(BASE_URL);
            const data = await response.json();

            listContainer.innerHTML = '';
            Object.entries(data).forEach(([taskId, task]) => {
                createTaskElement(task, taskId);
            });
        } catch (error) {
            console.error(error);
        }
    }

    async function addWeatherHandler() {
        const location = locationInput.value.trim();
        const temperature = temperatureInput.value.trim();
        const date = dateInput.value.trim();

        if (!location || !temperature || !date) {
            return;
        }

        const weatherData = {
            location,
            temperature,
            date,
        };

        const headers = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(weatherData),
        };

        try {
            await fetch(BASE_URL, headers);
            clearInputFields();
            loadHistoryHandler();
        } catch (error) {
            console.error(error);
        }
    }

    async function editWeatherHandler() {
        const location = locationInput.value.trim();
        const temperature = temperatureInput.value.trim();
        const date = dateInput.value.trim();

        if (!location || !temperature || !date) {
            return;
        }

        const selectedTaskId = editWeatherBtn.getAttribute('data-id');

        const headers = {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                location,
                temperature,
                date,
            }),
        };

        try {
            await fetch(BASE_URL + selectedTaskId, headers);
            clearInputFields();
            loadHistoryHandler();
            editWeatherBtn.disabled = true;
            addWeatherBtn.disabled = false;
        } catch (error) {
            console.error(error);
        }
    }

    function createTaskElement(task, taskId) {
        const taskElement = document.createElement('div');
        taskElement.className = 'container';
        taskElement.innerHTML = `
            <h2>${task.location}</h2>
            <h3>${task.date}</h3>
            <h3 id="celsius">${task.temperature}</h3>
            <div class="buttons-container">  
                <button class="change-btn" data-id="${taskId}">Change</button>
                <button class="delete-btn" data-id="${taskId}">Delete</button>
            </div>
        `;

        const changeBtn = taskElement.querySelector('.change-btn');
        const deleteBtn = taskElement.querySelector('.delete-btn');

        changeBtn.addEventListener('click', editTaskHandler);
        deleteBtn.addEventListener('click', deleteTaskHandler);

        listContainer.appendChild(taskElement);
    }

    function editTaskHandler(event) {
        const taskId = event.target.getAttribute('data-id');
        const task = event.target.parentElement.parentElement;
        const location = task.querySelector('h2').textContent;
        const date = task.querySelector('h3').textContent;
        const temperature = task.querySelector('#celsius').textContent;

        locationInput.value = location;
        temperatureInput.value = temperature;
        dateInput.value = date;

        editWeatherBtn.disabled = false;
        editWeatherBtn.setAttribute('data-id', taskId);
        addWeatherBtn.disabled = true;
    }

    async function deleteTaskHandler(event) {
        const taskId = event.target.getAttribute('data-id');

        const headers = {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
        };

        try {
            await fetch(BASE_URL + taskId, headers);
            loadHistoryHandler();
        } catch (error) {
            console.error(error);
        }
    }

    function clearInputFields() {
        locationInput.value = '';
        temperatureInput.value = '';
        dateInput.value = '';
    }
}
