var running = false;

function send() {
  if (running == true) return;
  var msg = document.getElementById("message").value ? document.getElementById("message").value:"";
  if (msg == "") return;
  running = true;
  addMsg(msg);


const url = 'http://localhost:5005/webhooks/rest/webhook';
let bodyh = JSON.stringify({
    "sender": "Prakash",  // sender ID of the user sending the message
    "message": msg
  })
// console.log(bodyh)
// Data to be sent in the request body

  
    // Send POST request and handle the response
     fetch("http://localhost:5005/webhooks/rest/webhook", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: bodyh
      })
      .then(response => response.json())
      .then(data => {
        console.log(data)

        for(x=0;x<data.length;x++){
        if(data[x].hasOwnProperty('text')){
            console.log(data[x].text)
            addResponseMsg(data[x].text);
        }
        if(data[x].hasOwnProperty('image')){
            addResponseMsgImage(data[x].image);
        }
        }
        // Use the response message as a response from the chatbot
        
      })
      .catch(error => {
        console.error("Error sending POST request:", error);
      })
      .finally(() => {
        running = false;
      });
    }

//         const requestData = {
//           sender: "Prakash", // sender ID of the user sending the message
//           message: "hello"
//         };
      
//         console.log(requestData)
//         axios.post("http://192.168.0.115:5005/webhooks/rest/webhook", requestData, {
//           headers: {
//             "Content-Type": "application/json"
//           }
//         })
//         .then(response => {
//           console.log(response.data.response);
//           // Use the response message as a response from the chatbot
//           addResponseMsg(response.data.response.message);
//         })
//         .catch(error => {
//           console.error("Error sending POST request:", error);
//         })
//         .finally(() => {
//           running = false;
//         });

// }
     
function addMsg(msg) {
  var div = document.createElement("div");
  console.log(msg)
  div.innerHTML =
    "<span style='flex-grow:1'></span><div class='chat-message-sent'>" +
    msg +
    "</div>";
  div.className = "chat-message-div";
  document.getElementById("message-box").appendChild(div);
  //SEND MESSAGE TO API
  document.getElementById("message").value = "";
  document.getElementById("message-box").scrollTop = document.getElementById(
    "message-box"
  ).scrollHeight;
}
function addResponseMsg(msg) {
  var div = document.createElement("div");
  div.innerHTML = "<div class='chat-message-received'>" + msg + "</div>";
  console.log(div)
  div.className = "chat-message-div";
  document.getElementById("message-box").appendChild(div);
  document.getElementById("message-box").scrollTop = document.getElementById(
    "message-box"
  ).scrollHeight;
  running = false;
}
function addResponseMsgImage(msg) {
    var div = document.createElement("div");
    var img = document.createElement("img");
    img.src = msg;
    div.appendChild(img);
    console.log(div)
    img.className = "chat-message-received-image"
    div.className ="chat-message-div";
    document.getElementById("message-box").appendChild(div);
    document.getElementById("message-box").scrollTop = document.getElementById(
      "message-box"
    ).scrollHeight;
    running = false;
  }
document.getElementById("message").addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    send();
  }
});
 document.getElementById("chatbot_toggle").onclick = function () {
    if (document.getElementById("chatbot").classList.contains("collapsed")) {
      document.getElementById("chatbot").classList.remove("collapsed")
      document.getElementById("chatbot_toggle").children[0].style.display = "none"
      document.getElementById("chatbot_toggle").children[1].style.display = ""
      setTimeout(addResponseMsg,500,"Hey there! It's me, a bot powered by Rasa. I'm designed to assist you by providing accurate information and addressing your corona related queries. Feel free to engage with me")
    }
    else {
      document.getElementById("chatbot").classList.add("collapsed")
      document.getElementById("chatbot_toggle").children[0].style.display = ""
      document.getElementById("chatbot_toggle").children[1].style.display = "none"
    }
  }
