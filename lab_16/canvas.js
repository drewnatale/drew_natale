function mouse()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    window.addEventListener("mousemove", icon, false);
}

function icon(e) {
    canvas.clearRect(0, 0, 600, 600);
    var xPos = e.clientX;
    var yPos = e.clientY;
    var pic = new Image();
    pic.src = "https://www.petinfoclub.com/Images/Albiventris%20shutterstock_65206192.jpg";
    canvas.drawImage(pic, xPos, yPos, 100, 100);
}
window.addEventListener("load", mouse, false);

