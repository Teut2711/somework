Object.values(document.getElementsByClassName("nav-link")).filter((ele)=>{
    return ele.textContent == "Query";
    })[0].classList.add("active");