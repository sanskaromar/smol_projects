let timerInterval;
let isRunning = false;
let minutes = 25;
let seconds = 0;

function updateDisplay() {
  const timerDisplay = document.getElementById("timer");
  timerDisplay.textContent = `${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
}

function startTimer() {
  if (!isRunning) {
    timerInterval = setInterval(function () {
      if (minutes === 0 && seconds === 0) {
        clearInterval(timerInterval);
        isRunning = false;
        alert("Time's up!");
        return;
      }
      if (seconds === 0) {
        minutes--;
        seconds = 59;
      } else {
        seconds--;
      }
      updateDisplay();
    }, 1000);
    isRunning = true;
  }
}

function resetTimer() {
  clearInterval(timerInterval);
  minutes = 25;
  seconds = 0;
  updateDisplay();
  isRunning = false;
}

document.getElementById("start").addEventListener("click", startTimer);
document.getElementById("reset").addEventListener("click", resetTimer);

updateDisplay();
