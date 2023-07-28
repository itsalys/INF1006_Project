window.addEventListener("load", (event) =>{
    sessionStorage.setItem('securityURL', "");
    sessionStorage.setItem('deliveryURL', "");
});

if(sessionStorage.getItem('securityURL') == null){
    sessionStorage.setItem('securityURL', "");
}

if(sessionStorage.getItem('deliveryURL') == null){
    sessionStorage.setItem('deliveryURL', "");
}

function createSecurityNotifCard(ts){

    const secNotifsList = document.getElementById("sec-notifs-list");

    const notifDiv = document.createElement("div");
    notifDiv.classList.add('notif-div', 'sec-notif-div');

    const notifCard = document.createElement("div");
    notifCard.className = "notif-card"

    const notifTop = document.createElement("div");
    notifTop.className = "notif-top";

    const notifLeft = document.createElement("div");
    notifLeft.className = "notif-left";

    const timeStampDiv = document.createElement("div");
    timeStampDiv.className = "time-stamp-div";

    const timeStamp = document.createElement("p");
    timeStamp.className = "time-stamp";
    timeStamp.textContent = ts;

    const notifRight = document.createElement("div");
    notifRight.className = "notif-right";

    const notifCloseDiv = document.createElement("div");
    notifCloseDiv.className = "notif-close-div";

    const notifClose = document.createElement("button");
    notifClose.className = "notif-close"

    const notifX = document.createElement("img");
    notifX.className = "notif-x"
    notifX.src = "../static/svg/x.svg"

    const notifBtm = document.createElement("div");
    notifBtm.className = "notif-btm";

    const notifContent = document.createElement("div");
    notifContent.className = "notif-content";

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

function createDeliveryNotifCard(ts){

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
    timeStamp.textContent = ts;

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

function load() {
    console.log("Loading");
    $.get("/process/sub", function (data) {
        const securityList = [];
        const deliveryList = [];

        const secTimeStamp = [];
        const delTimeStamp = [];

        // If the received data is a JavaScript object, handle it
        if (typeof data === "object") {
            
            mqttMessage = JSON.stringify(data);
        // $("#mqtt-message").html("MQTT Message: " + mqttMessage);
            // Loop through all the received messages
            for (var i = 0; i < data.length; i++) {
                var msg = data[i];
                console.log("This is the topic: ", msg.topic);
                // Check the topic and adjust the checkboxes accordingly

                if(msg.topic == "Doorway/Security"){
                    console.log("Security Index: ", i);
                    console.log("Security Time Stamp String", String(msg.mqttdata.timestamp));
                    secTimeStamp.push(String(msg.mqttdata.timestamp));
                    securityList.push(String(msg.mqttdata.picture));

                }
                else if(msg.topic == "Doorway/Delivery"){
                    console.log("Delivery Index: ", i);
                    console.log("Delivery Time Stamp String", String(msg.mqttdata.timestamp));
                    delTimeStamp.push(String(msg.mqttdata.timestamp));
                    deliveryList.push(String(msg.mqttdata.picture));

                }

            }

            const recentSecurity = securityList.pop();
            const recentDelivery = deliveryList.pop();

            console.log("Security Time Stamp List: ", secTimeStamp);
            console.log("Delivery Time Stamp List: ", delTimeStamp);

            const securityTS = secTimeStamp.pop();
            const deliveryTS = delTimeStamp.pop();

            console.log("Security Time Stamp: ", securityTS);
            console.log("Delivery Time Stamp: ", deliveryTS);

            const pastSecurityURL =  sessionStorage.getItem('securityURL');
            const pastDeliveryURL =  sessionStorage.getItem('deliveryURL');
            
            if(recentSecurity != pastSecurityURL){
                sessionStorage.setItem('securityURL', recentSecurity );
                $('#secfeed-img').attr("src", "data:image/jpg;base64," + recentSecurity);
                createSecurityNotifCard(securityTS);
            }

            if(recentDelivery != pastDeliveryURL){
                sessionStorage.setItem('deliveryURL', recentDelivery );
                $('#delfeed-img').attr("src", "data:image/jpg;base64," + recentDelivery);
                createDeliveryNotifCard(deliveryTS);
            } 

        }
    });
}

function imageError(id){
    image = document.getElementById(id);
    image.style.display = "none";
    
    if (id == "secfeed-img"){
        placeholder = document.getElementById("sec-img-placeholder")
        placeholder.style.display = "block";
    }
    else if(id == "delfeed-img"){
        placeholder = document.getElementById("del-img-placeholder")
        placeholder.style.display = "block";
    
    }
    

}

function imageLoad(id){
    image = document.getElementById(id);
    image.style.display = "block";
    
    if (id == "secfeed-img"){
        placeholder = document.getElementById("sec-img-placeholder")
        placeholder.style.display = "none";
    }
    else if(id == "delfeed-img"){
        placeholder = document.getElementById("del-img-placeholder")
        placeholder.style.display = "none";
    
    }

}

$(document).ready(function() {
    setInterval(function(){
        load();
    }, 5000);
    setInterval(function(){
        console.log("Test");
    }, 5000)
});

//Back Up Function Load

// function load() {
//     console.log("Loading");
//     $.get("/process/sub", function (data) {
//         const securityList = [];
//         const deliveryList = [];

//         // If the received data is a JavaScript object, handle it
//         if (typeof data === "object") {
//         mqttMessage = JSON.stringify(data);
//         // $("#mqtt-message").html("MQTT Message: " + mqttMessage);
//             // Loop through all the received messages
//             for (var i = 0; i < data.length; i++) {
//                 var msg = data[i];
//                 console.log("This is the topic: ", msg.topic);
//                 // Check the topic and adjust the checkboxes accordingly

//                 if(msg.topic == "Doorway/Security"){

//                     //Check if there is any images already in security
//                     const len = securityList.length 

                    


//                     securityList.push(String(msg.mqttdata.picture));
//                     console.log("Security Index: ", i);
//                     const secNotifsList = document.getElementById("sec-notifs-list");

//                     console.log("REACHED SECURITY");

//                     const sec_temp = sessionStorage.getItem('securityURL');
//                     if(String(msg.mqttdata.picture) !== sec_temp){
//                         console.log('This does not match, security');
//                         createSecurityNotifCard(String(msg.mqttdata.timestamp));
//                         //sessionStorage.setItem('securityURL', String(msg.mqttdata.picture) )
//                         $('#secfeed-img').attr("src", "data:image/jpg;base64," + String(msg.mqttdata.picture));
//                     }
//                     else{
                        
//                         console.log('This matches, security');
//                         sessionStorage.setItem('securityURL', String(msg.mqttdata.picture) )
//                         if (!secNotifsList.hasChildNodes()){
//                             createSecurityNotifCard(String(msg.mqttdata.timestamp));
//                         }
//                         $('#secfeed-img').attr("src", "data:image/jpg;base64," + String(msg.mqttdata.picture));
//                     }

//                     //break;

//                 }
//                 else if(msg.topic == "Doorway/Delivery"){
//                     deliveryList.push(String(msg.mqttdata.picture));
//                     console.log("Delivery Index: ", i);
//                     console.log("REACHED DELIVERY");
//                     const delNotifsList = document.getElementById("del-notifs-list");

//                     const del_temp = sessionStorage.getItem('deliveryURL');
//                     if(String(msg.mqttdata.picture) !== del_temp){
//                         console.log('This does not match, delivery');
//                         createDeliveryNotifCard(String(msg.mqttdata.timestamp));
//                         sessionStorage.setItem('deliveryURL', '' )
//                         sessionStorage.setItem('deliveryURL', String(msg.mqttdata.picture) )
//                         $('#delfeed-img').attr("src", "data:image/jpg;base64," + String(msg.mqttdata.picture));
//                     }
//                     else{
//                         console.log('This matches, delivery');
//                         sessionStorage.setItem('deliveryURL', String(msg.mqttdata.picture) )
//                         if (!delNotifsList.hasChildNodes()){
//                             createDeliveryNotifCard(String(msg.mqttdata.timestamp));
//                         }
//                         $('#delfeed-img').attr("src", "data:image/jpg;base64," + String(msg.mqttdata.picture));
//                     }
                    
                    
//                     //break;
//                 }

//                 // switch (msg.topic) {
                    
//                 //     case "Doorway/Security":
//                 //         const secNotifsList = document.getElementById("sec-notifs-list");

//                 //         console.log("REACHED SECURITY");
//                 //         const sec_temp = sessionStorage.getItem('securityURL');
//                 //         if(String(msg.mqttdata.picture) !== sec_temp){
//                 //             console.log('This does not match, security');
//                 //             createSecurityNotifCard(String(msg.mqttdata.timestamp));
//                 //             sessionStorage.setItem('securityURL', String(msg.mqttdata.picture) )
//                 //             $('#secfeed-img').attr("src", "data:image/jpg;base64," + String(msg.mqttdata.picture));
//                 //         }
//                 //         else{
//                 //             console.log('This matches, security');
//                 //             sessionStorage.setItem('securityURL', String(msg.mqttdata.picture) )
//                 //             if (!secNotifsList.hasChildNodes()){
//                 //                 createSecurityNotifCard(String(msg.mqttdata.timestamp));
//                 //             }
//                 //             $('#secfeed-img').attr("src", "data:image/jpg;base64," + String(msg.mqttdata.picture));
//                 //         }
                        
//                 //         break;

//                 //     case "Doorway/Delivery":
//                 //         console.log("REACHED DELIVERY");
//                 //         const delNotifsList = document.getElementById("del-notifs-list");

//                 //         const del_temp = sessionStorage.getItem('deliveryURL');
//                 //         if(String(msg.mqttdata.picture) !== del_temp){
//                 //             console.log('This does not match, delivery');
//                 //             createDeliveryNotifCard(String(msg.mqttdata.timestamp));
//                 //             sessionStorage.setItem('deliveryURL', '' )
//                 //             sessionStorage.setItem('deliveryURL', String(msg.mqttdata.picture) )
//                 //             $('#delfeed-img').attr("src", "data:image/jpg;base64," + String(msg.mqttdata.picture));
//                 //         }
//                 //         else{
//                 //             console.log('This matches, delivery');
//                 //             sessionStorage.setItem('deliveryURL', String(msg.mqttdata.picture) )
//                 //             if (!delNotifsList.hasChildNodes()){
//                 //                 createDeliveryNotifCard(String(msg.mqttdata.timestamp));
//                 //             }
//                 //             $('#delfeed-img').attr("src", "data:image/jpg;base64," + String(msg.mqttdata.picture));
//                 //         }
                        
                        
//                 //         break;

//                 // }
//             }

//             const recentSecurity = securityList.pop();
//             const recentDelivery = deliveryList.pop();

//             sessionStorage.setItem('securityURL', recentSecurity );
//             sessionStorage.setItem('deliveryURL', recentDelivery );

//         }
//     });
// }