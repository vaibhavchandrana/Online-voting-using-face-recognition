//code for pop up 
let popup=document.getElementById("popup");
function openpopup()
{
    popup.classList.add("open-pop-up");
}
function closepopup()
{
    popup.classList.remove("open-pop-up");
}

//code for voting the candidates 
function vote1()
{
    document.getElementById("first-candidate").value=1;
    var btn1 = document.getElementById("first");
    btn1.style.backgroundColor="#2196f3";
    btn1.style.color="white";
    document.getElementById("second-candidate").value=0;
    document.getElementById("third-candidate").value=0;
    var btn2 = document.getElementById("second");
    btn2.style.color="#2196f3";
    btn2.style.backgroundColor="white";
    var btn3 = document.getElementById("third");
    btn3.style.color="#2196f3";
    btn3.style.backgroundColor="white";
   
}
function vote2()
{
    document.getElementById("second-candidate").value=2;
    var btn = document.getElementById("second");
    btn.style.backgroundColor="#2196f3";
    btn.style.color="white";
    document.getElementById("first-candidate").value=0;
    document.getElementById("third-candidate").value=0;
    var btn2 = document.getElementById("first");
    btn2.style.color="#2196f3";
    btn2.style.backgroundColor="white";
    var btn3 = document.getElementById("third");
    btn3.style.color="#2196f3";
    btn3.style.backgroundColor="white";
   
}
function vote3()
{
    document.getElementById("third-candidate").value=3;
    var btn = document.getElementById("third");
    btn.style.backgroundColor="#2196f3";
    btn.style.color="white";
    document.getElementById("first-candidate").value=0;
    document.getElementById("second-candidate").value=0;
    var btn2 = document.getElementById("second");
    btn2.style.color="#2196f3";
    btn2.style.backgroundColor="white";
    var btn3 = document.getElementById("first");
    btn3.style.color="#2196f3";
    btn3.style.backgroundColor="white";
}
//code for pop up on submit button 
function subbtn()
{
   var b= document.getElementById("subbtn")
   b.style.backgroundColor=black;
   openpopup();

}

