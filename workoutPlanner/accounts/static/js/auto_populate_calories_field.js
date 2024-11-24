document.addEventListener("input", function () {
        const weight = parseFloat(document.getElementById("id_weight").value) || 0;
        const height = parseFloat(document.getElementById("id_height").value) || 0;

        const neededCalories = (10 * weight + 6.25 * height - 5 * 25).toFixed(2); // Adjust formula as needed
        document.getElementById("id_calories_needed").value = neededCalories;
    });