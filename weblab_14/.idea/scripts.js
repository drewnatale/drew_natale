
function validate() {
    var x = document.forms.input.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");

    //we naeed... username@webAddress.extension
    //if, the following...
        //@ is not in the string
        //@ is in the wrong place
        //there is no .com, .gov, or other extension
        //final dot is in the wrong place
    if(atPos < 1 || dotPos < atPos+2 || dotPos + 2 > x.length)
        alert("this is not a valid email address");

    else
        alert("success");

}

function validate() {
    var x = characters.6;
    
}






























