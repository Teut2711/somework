Object.values(document.getElementsByClassName("nav-link")).filter((ele)=>{
    return ele.textContent == "E-mail";
    })[0].classList.add("active");
    document.querySelector('.custom-file-input').addEventListener('change', (event) => {
        document.querySelector('.custom-file-label').textContent = event.target.files[0]["name"];
    });
     