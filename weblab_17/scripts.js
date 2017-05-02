function drag() {
    roses = document.getElementById("roses");
    leftBox = document.getElementById("leftBox");

    roses.addEventListener("dragstart", startDrag, false);


    leftBox.addEventListener("dragenter", dragEnter, false);
    leftBox.addEventListener("dragleave",dragLeave, false);
    leftBox.addEventListener("drgover", function(e){e.preventDefault()}, false);
    leftBox.addEventListener("drop", drop, false);
    roses.addEventListener("dragend", endDrag, false);
}

function startDrag(e)
{
    var pic = '<img id = "roses" src = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSlYxh5BEnSgKUQnVs8vqSSEx1m-cHWqFciGXSYmDEy-9dvGuKUQw">';
    e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e) {
    e.preventDefault();
    leftbox.style.background = "grey";
    leftbox.style.border = "3px solid black";
}

function dragLeave(e) {
    e.preventDefault();
    leftbox.style.background = "white";
    leftbox.style.border = "3px solid black";
}

function drop(e) {
    e.preventDefault();
    leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e)
{
    pic = e.target
    pic.style.visibility = "hidden";
}

window.addEventListener("load", drag, false);