allButtons = document.querySelectorAll('.buy')
console.log("allButtons =", allButtons)
// let countProduct = 0
let chosenId = []

function removeDuplicates(array) {
    return Array.from(new Set(array));
}

for (let count = 0; count < allButtons.length; count++){
    let button = allButtons[count]
    button.addEventListener(
        type = 'click',
        listener = function(){
            console.log("button.id =", button.id);
            if (document.cookie == ''){
                document.cookie = `products = ${button.id}; path = /`
                // countProduct++
                chosenId.push(button.id)
            }else{
                currentCookie = document.cookie.split('=')[1]
                
                document.cookie = `products = ${currentCookie} ${button.id}; path = /`

                // countProduct++
                chosenId.push(button.id)
            }
            // console.log("chosenId =", chosenId)
            
            let countProduct = removeDuplicates(chosenId)
            // console.log("countProduct.length = ", countProduct.length)
            // console.log("countProduct =", countProduct)
            let round = document.querySelector(".cart")
            round.innerText = countProduct.length
            round.id = "active-cart"
        }
    )
}