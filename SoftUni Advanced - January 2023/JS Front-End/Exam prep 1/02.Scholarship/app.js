window.addEventListener("load", solve);

function solve() {
  const nextBtn = document.getElementById("next-btn");
  const previewList = document.getElementById("preview-list");
  const candidatesList = document.getElementById("candidates-list");

  nextBtn.addEventListener("click", handleNextButtonClick);

  function handleNextButtonClick() {
    const studentInput = document.getElementById("student");
    const universityInput = document.getElementById("university");
    const scoreInput = document.getElementById("score");

    const studentName = studentInput.value.trim();
    const university = universityInput.value.trim();
    const score = scoreInput.value.trim();

    if (studentName === "" || university === "" || score === "") {
      return;
    }

    const li = document.createElement("li");
    li.classList.add("application");

    const article = document.createElement("article");

    const h4 = document.createElement("h4");
    h4.textContent = studentName;

    const pUniversity = document.createElement("p");
    pUniversity.textContent = `University: ${university}`;

    const pScore = document.createElement("p");
    pScore.textContent = `Score: ${score}`;

    article.appendChild(h4);
    article.appendChild(pUniversity);
    article.appendChild(pScore);

    const editBtn = document.createElement("button");
    editBtn.classList.add("action-btn", "edit");
    editBtn.textContent = "edit";
    editBtn.addEventListener("click", () => handleEditButtonClick(li, studentName, university, score));

    const applyBtn = document.createElement("button");
    applyBtn.classList.add("action-btn", "apply");
    applyBtn.textContent = "apply";
    applyBtn.addEventListener("click", () => handleApplyButtonClick(li));

    li.appendChild(article);
    li.appendChild(editBtn);
    li.appendChild(applyBtn);

    previewList.appendChild(li);

    studentInput.value = "";
    universityInput.value = "";
    scoreInput.value = "";

    nextBtn.disabled = true;
  }

  function handleEditButtonClick(li, studentName, university, score) {
    nextBtn.disabled = false;

    previewList.removeChild(li);

    document.getElementById("student").value = studentName;
    document.getElementById("university").value = university;
    document.getElementById("score").value = score;
  }

  function handleApplyButtonClick(li) {
    const editBtn = li.querySelector(".edit");
    const applyBtn = li.querySelector(".apply");

    li.removeChild(editBtn);
    li.removeChild(applyBtn);

    candidatesList.appendChild(li);

    nextBtn.disabled = false;
  }
}
