//Vanish the formclass and the loader from the DOM
document.querySelector(".formclass").style.display = "none";
document.querySelector(".lds-ring").style.display = "none";


//'Active' class added to 'Master' navbar tab
Object.values(document.getElementsByClassName("nav-link")).filter((ele) => {
    return ele.textContent == "Master";
})[0].classList.add("active");


// If a button is clicked dom creates its page
document.querySelector('.cdslbenpos>li').addEventListener('click', function (event) {
    var ele = document.querySelector('.mainbox').querySelector(".nsdlbenpos");
    ele.parentNode.removeChild(ele);
    document.querySelector('.formclass').style.cssText = 'display:flex';
    document.querySelector("input[name='hidden']").setAttribute("value",  'cdslbenpos');
})

document.querySelector('.nsdlbenpos>li').addEventListener('click', function (event) {
    var ele = document.querySelector('.mainbox').querySelector(".cdslbenpos");
    ele.parentNode.removeChild(ele);
    document.querySelector('.formclass').style.cssText = 'display:flex';
    document.querySelector("input[name='hidden']").setAttribute("value",  'nsdlbenpos');
})



// fetch post request
document.querySelector("form").addEventListener('submit', function(event){
    
    event.preventDefault();
    console.log(event.currentTarget)
    var formData = new FormData(event.currentTarget);
    console.log(formData);
    
    fetch("http://127.0.0.1:8000/master/", {
        method: "post",
        body: formData
    }).then(function (response) {
        document.querySelector(".lds-ring").remove();
        console.log(response)
        document.querySelector(".formclass").insertAdjacentHTML('beforeend', "<h1>Process Completed</h1>");

    }).catch(function (response) {
        console.log("Error");
    })

    //
    document.querySelector(".lds-ring").style.display = "flex";
    document.getElementsByClassName("submitfile")[0].remove();
})

