//Vanish the formclass and the loader from the DOM
document.querySelector(".formclass").style.display = "none";
document.querySelector(".loader").style.display = "none";


//'Active' class added to 'Master' navbar tab
Object.values(document.getElementsByClassName("nav-link")).filter((ele) => {
    return ele.textContent == "Master";
})[0].classList.add("active");


// If a button is clicked dom creates its page
document.querySelector('.cdslbenpos>li').addEventListener('click', function (event) {
    var ele = document.querySelector('.mainbox').querySelector(".nsdlbenpos");
    ele.parentNode.removeChild(ele);
    document.querySelector('.formclass').style.cssText = 'display:flex';
    document.querySelector("input[type='hidden']").setAttribute('value', 'cdslbenpos');
})

document.querySelector('.nsdlbenpos>li').addEventListener('click', function (event) {
    var ele = document.querySelector('.mainbox').querySelector(".cdslbenpos");
    ele.parentNode.removeChild(ele);
    document.querySelector('.formclass').style.cssText = 'display:flex';
    document.querySelector("input[type='hidden']").setAttribute('value', 'nsdlbenpos');
})



// fetch post request
document.querySelector("form")[0].addEventListener('submit', function (ele) {
    ele.preventDefault();
    var formData = new FormData(ele.currentTarget);

    fetch("http://127.0.0.1:8000/master/", {
        method: "post",
        body: formData
    }).then(function (response) {
        document.querySelector(".loader").remove();
        document.querySelector(".formclass").insertAdjacentHTML('beforeend', "<h1>Process Completed</h1>");

    }).catch(function (response) {
        console.log("Error");
    })

    //
    document.querySelector(".loader").style.display = "flex";
    document.getElementsByClassName("submitfile")[0].remove();
})

