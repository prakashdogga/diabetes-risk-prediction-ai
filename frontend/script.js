const form = document.getElementById("risk-form");
const resultCard = document.getElementById("result-card");
const riskPill = document.getElementById("risk-pill");
const probabilityValue = document.getElementById("probability-value");
const adviceText = document.getElementById("advice-text");

// FastAPI endpoint
const API_URL = "http://localhost:8000/predict";

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const payload = {
    pregnancies: Number(document.getElementById("pregnancies").value),
    glucose: Number(document.getElementById("glucose").value),
    blood_pressure: Number(document.getElementById("blood_pressure").value),
    skin_thickness: Number(document.getElementById("skin_thickness").value),
    insulin: Number(document.getElementById("insulin").value),
    bmi: Number(document.getElementById("bmi").value),
    diabetes_pedigree: Number(document.getElementById("diabetes_pedigree").value),
    age: Number(document.getElementById("age").value),
  };

  try {

    const res = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (!res.ok) {
      throw new Error("Server error");
    }

    const result = await res.json();

    const prob = result.probability;
    const risk = result.risk;

    probabilityValue.textContent = (prob * 100).toFixed(2) + "%";
    riskPill.textContent = "Risk: " + risk;

    riskPill.classList.remove("risk-low", "risk-moderate", "risk-high");

    if (risk === "High") {
      riskPill.classList.add("risk-high");
      adviceText.textContent =
        "High diabetes risk detected. Please consult a healthcare professional immediately.";
    } 
    else if (risk === "Moderate") {
      riskPill.classList.add("risk-moderate");
      adviceText.textContent =
        "Moderate risk detected. Consider improving diet, exercise, and regular health checkups.";
    } 
    else {
      riskPill.classList.add("risk-low");
      adviceText.textContent =
        "Low risk detected. Maintain a healthy lifestyle and routine screenings.";
    }

    resultCard.hidden = false;

  } catch (error) {

    console.error("Error:", error);

    alert("Failed to get prediction. Make sure the FastAPI server is running.");

  }
});