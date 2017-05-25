function shapes()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    canvas.strokeStyle = "";
    canvas.fillStyle = "blue";
    canvas.beginPath();
    canvas.moveTo(50, 50);
    canvas.lineTo(50, 50);
    canvas.lineTo(50, 90);
    canvas.lineTo(90, 100);
    canvas.lineTo(100, 100);
    canvas.lineTo(100,100);
    canvas.lineTo(100,100);
    canvas.lineTo(200, 150);
    canvas.lineTo(200, 300);
    canvas.lineTo(300, 200);
    canvas.lineTo(100,100);
    canvas.lineTo(100, 100);



    canvas.stroke();



}

window.addEventListener("load", shapes, false);