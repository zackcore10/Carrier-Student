document.getElementById("careerForm").addEventListener("submit", async function(event) {

    event.preventDefault();

    let name = document.getElementById("name").value;
    let programming = document.getElementById("programming").value;
    let math = document.getElementById("math").value;
    let communication = document.getElementById("communication").value;
    let interest = document.getElementById("interest").value;
    let experience = document.getElementById("experience").value;

    try {

        let response = await fetch("http://127.0.0.1:8000/assessment", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                name: name,
                programming: programming,
                math: math,
                communication: communication,
                interest: interest,
                experience: experience
            })

        });

        let data = await response.json();

        let result = document.getElementById("result");

        result.style.display = "block";

        result.innerHTML = `
            <h2>🎯 ${data.recommended_career}</h2>

            <p><strong>Hello ${data.student.name}!</strong></p>

            <p>
                Based on your skills and interests,
                this career path could be suitable for you.
            </p>

            <p><strong>Your Profile:</strong></p>

            <p>Programming: ${data.student.programming}</p>
            <p>Mathematics: ${data.student.math}</p>
            <p>Communication: ${data.student.communication}</p>
            <p>Experience: ${data.student.experience}</p>
        `;

    } catch (error) {

        console.error(error);

        document.getElementById("result").innerHTML = `
            <p>❌ Could not connect to the CareerAI backend.</p>
        `;

        document.getElementById("result").style.display = "block";
    }

});