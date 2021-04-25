// menu button
var MenuItems = document.getElementById("MenuItems");

MenuItems.style.maxHeight = "0px";
function menutoggle(){
    if(MenuItems.style.maxHeight = "0px")
    {
        MenuItems.style.maxHeight = "200px";
    }
    else
    {
        MenuItems.style.maxHeight = "0px";
    }
}

// product details page
// switch between images
 var productimg = document.getElementById("productimg");
 var smallimg = document.getElementsByClassName("small-img"); //4 element array
 smallimg[0].onclick = function(){
    productimg.src = smallimg[0].src;
 }
 smallimg[1].onclick = function(){
    productimg.src = smallimg[1].src;
 }
 smallimg[2].onclick = function(){
    productimg.src = smallimg[2].src;
 }
 smallimg[3].onclick = function(){
    productimg.src = smallimg[3].src;
 }



//  login page

var loginform = document.getElementById("loginform");
var registerform = document.getElementById("registerform");
var Status = document.getElementById("status");

function register(){
   registerform.style.transform = "translateX(0px)";
   loginform.style.transform = "translateX(0px)";
   status.style.transform = "translateX(100px)";

}
function login(){
   registerform.style.transform = "translateX(300px)";
   loginform.style.transform = "translateX(300px)";
   status.style.transform = "translateX(0px)";
}

// ERROR: registorform is undefined