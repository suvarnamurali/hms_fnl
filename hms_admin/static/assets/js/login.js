const password = document.getElementById("password");
const form = document.getElementById("form");
const error = document.getElementById("error")


form.addEventListener("submit", (e) => {
    let messages = []
       if(password.value.length <= 5) {
        messages.push("Password is too short.")
    }

    if(password.value.length >= 20) {
        messages.push("Password is too long.")
    }

    if(messages.length > 0) {
        e.preventDefault()
        error.innerText = messages.join(", ")
    }
  })
