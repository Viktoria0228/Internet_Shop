const listButtonsMinus = document.querySelectorAll(".minus")

for (let count = 0; count < listButtonsMinus.length; count++){
    let button = listButtonsMinus[count]
    button.addEventListener(
        type = "click",
        listener = function(event) {
            let listIdProducts = document.cookie.split("=")[1].split(" ")

            for(let index = 0; index < listIdProducts.length; index++){
                if (listIdProducts[index] == button.id){
                    if (button.nextElementSibling.textContent > 1){
                        listIdProducts.splice(index, 1)
                        button.nextElementSibling.textContent = +button.nextElementSibling.textContent - 1
                        console.log(listIdProducts)

                        break
                    }
                }
            }
            document.cookie = `products=${listIdProducts.join(" ")}; path = /`

        }
    )
}

const listButtonPlus = document.querySelectorAll(".plus")

for(let count = 0; count < listButtonPlus.length; count++){
    // console.log(listButtonPlus)
    let button = listButtonPlus[count]
    button.addEventListener(
        type = "click",
        listener = function(event) {
            if (document.cookie == ""){
                document.cookie = `products = ${button.id}`
                button.previousElementSibling.textContent = +button.previousElementSibling.textContent + 1
                // console.log("1", button.id)
            }else{
                // console.log("2", button.id)
                let currentProduct = document.cookie.split("=")[1]
                document.cookie = `products = ${currentProduct} ${button.id}; path = /`
                button.previousElementSibling.textContent = +button.previousElementSibling.textContent + 1
                
            }
        }
    )
}


let listDeleteProducts = document.querySelectorAll(".delete")

for (let id = 0; id < listDeleteProducts.length; id++){
    console.log(listDeleteProducts)
    let button = listDeleteProducts[id]
    button.addEventListener(
        type = "click",
        listener = function(event){
           if (document.cookie != "") {
                // let buttonsID = button.id.split("-")[1]
                // console.log(button.id)

                let listIDProducts = document.cookie.split("=")[1].split(" ")
                let lenList = listIDProducts.length

                for (let a = 0; a < lenList; a++) {
                    for (let c = 0; c < lenList; c++) {
                        if (listIDProducts[c] === button.id) {
                            // console.log(c)
                            // console.log(lenList)
                            listIDProducts.splice(c, 1)
                            console.log(listIDProducts)
                        }
                    }
                }   
                // console.log(document.querySelector(`.delete`))
                console.log(document.getElementById(`${button.id}`))
                // console.log(document.querySelector(`.products`))
                document.getElementById(button.id).remove()
                // document.querySelector(".products").remove()
                // document.cookie = `products=${listIdProducts.join(" ")}; path = /`
                if (listIDProducts.length >= 0) {
                    // console.log(listIDProducts)
                    document.cookie = `products = ${listIDProducts.join(' ')}; path = /` 
                    // document.cookie = `products = ; path = /` 
                }
                if (document.cookie.split('=')[1] == ''){
                    let p = document.createElement("p")
                    p.textContent = "Корзина порожня😢"
                    document.body.append(p)
                    document.querySelector(".order").remove()
                }
            }
        }
    )
}





