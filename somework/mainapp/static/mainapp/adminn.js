Object.values(document.getElementsByClassName("nav-link")).filter((ele)=>{
    return ele.textContent == "Admin";
    })[0].classList.add("active");