const spamExample =
`Congratulations! You have won a free cash prize.
Click here to claim your reward immediately.
This is a limited time offer.`;

const normalExample =
`Hello,
Please remember that our college project meeting is scheduled for tomorrow at 10 AM.
Please bring your assignment notes.`;

function loadSpam() {
    document.getElementById("email").value = spamExample;
}

function loadHam() {
    document.getElementById("email").value = normalExample;
}

function clearAll() {
    document.getElementById("email").value = "";
    document.getElementById("result").classList.add("hidden");
    document.getElementById("error").classList.add("hidden");
}

async function checkEmail() {
    const text = document.getElementById("email").value.trim();
    const error = document.getElementById("error");
    const result = document.getElementById("result");
    const button = document.getElementById("checkBtn");

    error.classList.add("hidden");

    if (text.length < 5) {
        error.textContent = "Please enter a longer email message.";
        error.classList.remove("hidden");
        return;
    }

    button.disabled = true;
    button.textContent = "Checking...";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({email: text})
        });

        const data = await response.json();

        if (!response.ok) throw new Error(data.error || "Something went wrong.");

        result.classList.remove("hidden");

        const title = document.getElementById("resultTitle");
        title.textContent = data.result === "SPAM" ? "🚨 SPAM EMAIL" : "✅ NOT SPAM";

        document.getElementById("probability").textContent =
            data.spam_probability + "%";

        document.getElementById("barFill").style.width =
            data.spam_probability + "%";

        document.getElementById("words").textContent = data.analysis.words;
        document.getElementById("characters").textContent = data.analysis.characters;
        document.getElementById("links").textContent = data.analysis.links;
        document.getElementById("suspicious").textContent = data.analysis.suspicious;

    } catch (err) {
        error.textContent = err.message;
        error.classList.remove("hidden");
    } finally {
        button.disabled = false;
        button.textContent = "Check with AI";
    }
}
