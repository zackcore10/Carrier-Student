document.getElementById("careerForm").addEventListener("submit", function(event) {

    event.preventDefault();

    let name = document.getElementById("name").value;
    let programming = document.getElementById("programming").value;
    let math = document.getElementById("math").value;
    let communication = document.getElementById("communication").value;
    let interest = document.getElementById("interest").value;
    let experience = document.getElementById("experience").value;

    let career = "";

    if (interest === "Artificial Intelligence") {
        career = "AI/ML Engineer";
    }
    else if (interest === "Web Development") {
        career = "Full Stack Developer";
    }
    else if (interest === "Data Science") {
        career = "Data Scientist";
    }
    else if (interest === "Cyber Security") {
        career = "Cyber Security Analyst";
    }
    else if (interest === "Cloud Computing") {
        career = "Cloud Engineer";
    }

    let result = document.getElementById("result");

    result.style.display = "block";

    result.innerHTML = `
        <h2>🎯 ${career}</h2>

        <p><strong>Hello ${name}!</strong></p>

        <p>
            Based on your selected skills and interests,
            this career path could be suitable for you.
        </p>

        <p><strong>Your Profile:</strong></p>

        <p>Programming: ${programming}</p>
        <p>Mathematics: ${math}</p>
        <p>Communication: ${communication}</p>
        <p>Experience: ${experience}</p>
    `;

});