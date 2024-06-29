let buttonSubmit = document.querySelector(".registration_submit")
let regForm = document.querySelector("#registration_content")
buttonSubmit.addEventListener(
  type = "click",
  listener = function(event){
    let inputsFilled = true
    // event.preventDefault()
    for (let index = 0; index < regForm.elements.length; index++) { 
      let element = regForm.elements[index]; 
      if (!element.value){
        inputsFilled = false
       }
      if(inputsFilled){
        document.querySelector(".modal-window").style.display = "flex"
      }

      
    } 
    
  }
)


  
