
# Cyberhell Activity Tracker

## Submit Your Progress


<div class="progress">

Student Number: <input type="text" id="student-number" placeholder="Example: 2" required>  

**Question:** What is the name of the malware deployed using Teamsphisher?

**Answer:** formatted as `<File-Name>.<Extension>`, for example `text.txt`: <input type="text" id="answer" placeholder="Example: text.txt" required>  

<br>

<button onclick="submitProgress()" class="fancy-button">Submit</button>


<script>
    
function submitProgress() {
    const studentNumber = document.getElementById("student-number").value;
    const answer = document.getElementById("answer").value;
    const chapter = "3";

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
    fetch("http://192.168.253.138:8000/submit-3", { 
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