let buttonSend = document.querySelector(".authorization_submit")
let regForm = document.querySelector("#authorization_content")

buttonSend.addEventListener(
  type = "click",
  listener = function(event){
    let inputsFilled = true
    // event.preventDefault()
    console.log("button send.clicked")
    for (let index = 0; index < regForm.elements.length; index++) { 
      let element = regForm.elements[index]; 
      if (!element.value){
        inputsFilled = false
       }
      if(inputsFilled){
        document.querySelector(".modal-window").style.display = "flex"
      }
    // event.preventDefault()
    } 
  }
)
