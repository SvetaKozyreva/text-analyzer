document.getElementById("analyzeBtn").addEventListener("click", async () => {
    const text = document.getElementById("text").value;

    try {
        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        });

        if (!response.ok) throw new Error("Помилка сервера");

        const data = await response.json();
        document.getElementById("result").textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        document.getElementById("result").textContent = "Помилка: " + error.message;
    }
});