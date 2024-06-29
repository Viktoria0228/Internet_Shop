document.addEventListener(
    type = "DOMContentLoaded",
    listener = function(event){
        let listCountProducts = document.querySelectorAll('.products')
        let productCountId = document.getElementById('count-product')
        // let totalPriceId = document.getElementById('total-price')
        productCountId.textContent = listCountProducts.length
        // let listNumberPrices = []
        let totalPrice = 0
        let totalDiscount = 0
        
        // let listCountCount = []

        // let product = products[productPrice]
        let listProductPrices = document.querySelectorAll(".product-price")
        for(let productPrice = 0; productPrice < listProductPrices.length; productPrice++ ){
            console.log(listProductPrices[productPrice])
            // console.log("innerText =", productPrice.textContent)

            let listFullPrice = document.querySelectorAll(".invisible")
            for (fullPrice of listFullPrice){
                console.log("fullPrice.innerText =", fullPrice.textContent, "; Number(listProductPrices[productPrice].innerText.split()[0] =", Number(listProductPrices[productPrice].innerText.split(" ")[0]))
                let onlyNumberPrice = Number(fullPrice.textContent).toFixed(2)
                let elementId = listProductPrices[productPrice].id
                console.log("id =", elementId, document.getElementById(`quantity ${elementId}`).textContent)

                // listNumberPrices.push(onlyNumberPrice * document.getElementById(`quantity ${elementId}`).textContent)
                let quantity = Number(document.getElementById(`quantity ${elementId}`).textContent)
                let totalPriceResult = onlyNumberPrice * quantity

                // listNumberPrices.push(totalPriceResult.toFixed(2))
                totalPrice += totalPriceResult
                if (fullPrice.id == listProductPrices[productPrice].id){
                    discount = Number(fullPrice.textContent) - Number(listProductPrices[productPrice].innerText.split(" ")[0])
                    console.log("discount =", discount)
                    for (let count = 0; count < quantity; count++) {
                        totalDiscount += discount
                    }
                }
                
            }
            console.log(totalDiscount)
            document.getElementById("total-discount").innerText = `${totalDiscount.toFixed(2)} грн`
            
        }
        console.log("total price:", totalPrice)
        document.getElementById("total-price").textContent = `${totalPrice.toFixed(2)} `
        

        let totalTotalPrice = (totalPrice) - totalDiscount
        document.querySelector("#total-amount").textContent = `${totalTotalPrice.toFixed(2)} грн`
    }
)

let listPrice = document.querySelectorAll(".product-price")

for (let price of listPrice){
    console.log("price =", price)
    price.innerText = `${Number(price.innerText.split(" ")[0]).toFixed(2)} грн`
    console.log("price.innerText =", price.innerText)
}

let checkoutButton = document.querySelector(".checkout")


checkoutButton.addEventListener(
    type = "click",
    listener = function(event){
        event.preventDefault()
        document.querySelector(".placing").style.display = "flex"
        console.log("aaskasjinaso")
    }
)

let sendButton = document.createElement(".send-product")

sendButton.addEventListener(
    type = "click",
    listener = function(event){
        let all = document.querySelectorAll()
        all.remove()
        console.log("a")

        let h2 = document.createElement("h2")
        h2.classList.add("waiting-text")
        document.body.appendChild(h2)
    }
)