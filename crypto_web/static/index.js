window.onload = function(){
    setInterval(update, 5000);
    update()
  };
  
  function update(){
    fetch('/get_data')
          .then(function (response) {
              return response.json();
          }).then(function (text) {

            //update div
            var e = document.getElementById("crypto")
            e.innerHTML = text["data"]['name']

            //update div
            var e2 = document.getElementById("info")
            var info = text["data"]['price']
            info += "<br >" + text["data"]['per']
            info += "<br >" + text["data"]['day']
            e2.innerHTML = info
  
          });
  };