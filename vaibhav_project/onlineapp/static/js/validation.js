//function for form validation
function validate()
{
  //validation for name 
  var fn=document.getElementById("name").value;
  var reg1=/[a-zA-Z" "]{5,30}$/g;
  if(!reg1.test(fn))
  {
    document.getElementById("error1").innerHTML="* Name must contain letter from a-z";
    return false;   
  }
  //validation for phone
  var pn=document.getElementById("phone").value;
  var reg2=/^[0-9]{10}$/g;
  if(!reg2.test(pn))
  {
    document.getElementById("error2").innerHTML=" * write phone no in form XXXXXXXXXX ";
    return false;
  }
  var pass=document.getElementById("pass").value;
  var cpass=document.getElementById("cpass").value;
  // validation for password and confirm password
  if(pass.length<8||pass.length>15)
  {
    document.getElementById("error3").innerHTML="*8 character";
    return false;
  }
  if(pass!=cpass)
  {
    document.getElementById("error4").innerHTML="* password not matched";
    return false;
  }
}