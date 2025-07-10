
# Cyberhell Activity Tracker

## Submit Your Progress


<div class="progress">

Student Number: <input type="text" id="student-number" placeholder="Example: 2" required>  

**Question:**
Which technique is used to achieve Persistence on the system? (Example format: T1133.002)

ℹ️**Tip for the answer:**
Use the MITRE ATT&CK framework to find and enter the technique ID (e.g., T1133.002), not the technique name.

**Answer:** <input type="text" id="answer" placeholder="Example: T133.002" required>  

<button onclick="submitProgress()" class="fancy-button">Submit</button>


<script>
    
function submitProgress() {
    const studentNumber = document.getElementById("student-number").value;
    const answer = document.getElementById("answer").value;
    const chapter = "5";

    const number = Number(studentNumber.trim());

    if (number == "" ) {
        alert("❌ Student Number filed is empty. \nPlease provide your STUDENT-NUMBER");
        return;
    }

    if (isNaN(number) || number < 2 || number > 999 ) {
        alert("❌ Invalid Student Number, enter a number between 2 and 999 in the STUDENT-NUMBER field.");
        return;
    }

    // Send Data to FastAPI (Without the Answer)
    fetch("http://192.168.253.138:8000/submit-5", { 
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            "student_number": studentNumber, 
            "chapter": chapter,
            "answer": answer
        })
    })
    .then(response => {
        if (!response.ok) {
            // If error from server, parse the JSON error
            return response.json().then(data => { 
                throw new Error(data.detail); // detail is the field FastAPI uses for errors
            });
        }
        return response.json();
    })
    .then(data => alert(data.message)) // Success
    .catch(error => alert(error.message)); // Error
    
}
</script>

</div>