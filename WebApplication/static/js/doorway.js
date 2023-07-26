if(window.deliveryList == undefined){

}


function createSecurityNotifCard(){

    const secNotifsList = document.getElementById("sec-notifs-list");

    const notifDiv = document.createElement("div");
    notifDiv.classList.add('notif-div', 'sec-notif-div');

    const notifCard = document.createElement("div");
    notifCard.className = "notif-card"

    const notifTop = document.createElement("div");
    notifTop.className = "notif-top"

    const notifLeft = document.createElement("div");
    notifLeft.className = "notif-left"

    const timeStampDiv = document.createElement("div");
    timeStampDiv.className = "time-stamp-div"

    const timeStamp = document.createElement("p");
    timeStamp.className = "time-stamp"
    timeStamp.textContent = "09:04:58 10/03/2023"

    const notifRight = document.createElement("div");
    notifRight.className = "notif-right"

    const notifCloseDiv = document.createElement("div");
    notifCloseDiv.className = "notif-close-div"

    const notifClose = document.createElement("button");
    notifClose.className = "notif-close"

    const notifX = document.createElement("img");
    notifX.className = "notif-x"
    notifX.src = "../static/svg/x.svg"

    const notifBtm = document.createElement("div");
    notifBtm.className = "notif-btm"

    const notifContent = document.createElement("div");
    notifContent.className = "notif-content"

    const notifTxt = document.createElement("p");
    notifTxt.className = "notif-txt"
    notifTxt.textContent = "Someone is outside your door! Please check the feed."

    //Appending Divs and Elements

    timeStampDiv.appendChild(timeStamp);
    notifLeft.appendChild(timeStampDiv);

    notifClose.appendChild(notifX)
    notifCloseDiv.appendChild(notifClose);
    notifRight.appendChild(notifCloseDiv);

    notifTop.appendChild(notifLeft);
    notifTop.appendChild(notifRight);

    notifContent.appendChild(notifTxt);
    notifBtm.appendChild(notifContent);

    notifCard.appendChild(notifTop);
    notifCard.appendChild(notifBtm);

    notifDiv.appendChild(notifCard);

    secNotifsList.appendChild(notifDiv);
}

function createDeliveryNotifCard(){

    const delNotifsList = document.getElementById("del-notifs-list");

    const notifDiv = document.createElement("div");
    notifDiv.classList.add('notif-div', 'del-notif-div');

    const notifCard = document.createElement("div");
    notifCard.className = "notif-card"

    const notifTop = document.createElement("div");
    notifTop.className = "notif-top"

    const notifLeft = document.createElement("div");
    notifLeft.className = "notif-left"

    const timeStampDiv = document.createElement("div");
    timeStampDiv.className = "time-stamp-div"

    const timeStamp = document.createElement("p");
    timeStamp.className = "time-stamp"
    timeStamp.textContent = "09:04:58 10/03/2023"

    const notifRight = document.createElement("div");
    notifRight.className = "notif-right"

    const notifCloseDiv = document.createElement("div");
    notifCloseDiv.className = "notif-close-div"

    const notifClose = document.createElement("button");
    notifClose.className = "notif-close"

    const notifX = document.createElement("img");
    notifX.className = "notif-x"
    notifX.src = "../static/svg/x.svg"

    const notifBtm = document.createElement("div");
    notifBtm.className = "notif-btm"

    const notifContent = document.createElement("div");
    notifContent.className = "notif-content"

    const notifTxt = document.createElement("p");
    notifTxt.className = "notif-txt"
    notifTxt.textContent = "You have a delivery! Please check the feed for photos."

    //Appending Divs and Elements

    timeStampDiv.appendChild(timeStamp);
    notifLeft.appendChild(timeStampDiv);

    notifClose.appendChild(notifX)
    notifCloseDiv.appendChild(notifClose);
    notifRight.appendChild(notifCloseDiv);

    notifTop.appendChild(notifLeft);
    notifTop.appendChild(notifRight);

    notifContent.appendChild(notifTxt);
    notifBtm.appendChild(notifContent);

    notifCard.appendChild(notifTop);
    notifCard.appendChild(notifBtm);

    notifDiv.appendChild(notifCard);

    delNotifsList.appendChild(notifDiv);
}


$(document).ready(function() {

});