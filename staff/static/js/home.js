function myFunction() {
    var element = document.getElementById('home-body');
    element.classList.toggle("dark-mode");
  
    var x = document.getElementById("btnValue");
    if (x.innerHTML === "Dark mode") {
      x.innerHTML = "Light mode";
      x.classList.remove('btn-dark')
      x.classList.toggle('btn-light')
    } else {
      x.innerHTML = "Dark mode";
      x.classList.remove('btn-light')
      x.classList.toggle('btn-dark')
    }
  
  }
  