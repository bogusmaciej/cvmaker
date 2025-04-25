function addEducation() {
  const educationList = document.getElementById('education-list');
  const newEntry = document.createElement('div');
  newEntry.classList.add('education-entry');

  newEntry.innerHTML = `
    <div class="education-header">
        <button type="button" class="toggle-education" onclick="toggleEducation(this)">▼</button>
        <input type="text" name="school_name" value="Nowa szkoła" readonly>
        <button type="button" class="remove-education" onclick="removeEducation(this)">Usuń</button>
    </div>
    <div class="education-details">
        <input type="text" name="year_start" placeholder="Rok rozpoczęcia" required>
        <input type="text" name="year_end" placeholder="Rok zakończenia" required>
        <input type="text" name="major" placeholder="Kierunek" required>
        <input type="text" name="degree" placeholder="Stopień" required>
    </div>
    <hr>
  `;

  educationList.appendChild(newEntry);
  // Od razu rozwiń nowe wpisy
  toggleEducation(newEntry.querySelector('.toggle-education'));  
}

function toggleEducation(button) {
  const details = button.parentNode.nextElementSibling;
  const schoolNameInput = button.parentNode.querySelector('input[name="school_name"]');
  
  details.classList.toggle('show');
  const removeBtn = button.parentNode.querySelector('.remove-education');
  removeBtn.style.display = details.classList.contains('show') ? 'inline-block' : 'none';
  
  // Zmiana tekstu w przycisku rozwijania/zwijania
  if (details.classList.contains('show')) {
    button.textContent = '▲'; // Zwijanie
    schoolNameInput.removeAttribute('readonly');
  } else {
    button.textContent = '▼'; // Rozwijanie
    schoolNameInput.setAttribute('readonly', 'true');
  }
}

function removeEducation(button) {
  const educationEntry = button.closest('.education-entry');
  educationEntry.remove();
}