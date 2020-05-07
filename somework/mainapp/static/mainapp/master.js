Object.values(document.getElementsByClassName("nav-link")).filter((ele)=>{
    return ele.textContent == "Master";
    })[0].classList.add("active");

document.querySelector('.cdslbenpos>li').addEventListener('click', function(event){
       var ele  = document.querySelector('.mainbox').querySelector(".nsdlbenpos");
     ele.parentNode.removeChild(ele);
    document.querySelector('.formclass').style.cssText='display:flex;justify-content:center';
     document.getElementsByTagName("form")[0].insertAdjacentHTML('afterbegin','<input type="hidden" name="hidden" value="cdslbenpos">');


})   

document.querySelector('.nsdlbenpos>li').addEventListener('click', function(event){
    var ele  = document.querySelector('.mainbox').querySelector(".cdslbenpos");
     ele.parentNode.removeChild(ele);
    document.querySelector('.formclass').style.cssText='display:flex;justify-content:center';
    document.getElementsByTagName("form")[0].insertAdjacentHTML('afterbegin','<input type="hidden" name="hidden" value="nsdlbenpos">');
})
