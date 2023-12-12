function addItem() {
    input = document.getElementById('newItemText');
    const newLi = document.createElement('li');
    newLi.textContent = input.value;
    const deleteBtn = document.createElement('a');
    deleteBtn.href = '#';
    deleteBtn.textContent = '[Delete]';
    newLi.appendChild(deleteBtn);

    deleteBtn.addEventListener('click', () => newLi.remove());
    const list = document.getElementById('items');
    list.appendChild(newLi);
}