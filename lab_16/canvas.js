function mouse()
{
    varx = document.getElemantById("canvas");
    canvas = x.getContext("2d");


    window.addEventListner("mousemove", icon, false);
}


function text ()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");


    var pic = new Image();
    pic.src = "https://www.petinfoclub.com/Images/Albiventris%20shutterstock_65206192.jpg";


    pic.addEventListener("load", function() { canvas.drawImage(pic, 200, 200)}, false);
}

window.addEventListener("load", text, false);



