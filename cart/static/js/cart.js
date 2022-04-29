let btns = document.getElementsByClassName('addtocart')
for(let i =0; i<btns.length; i++){
  btns[i].addEventListener('click', function(e){
  let product_id = e.target.dataset.product
  let action = e.target.dataset.action
    if(user=="AnonymousUser"){
      console.log('Not Logged in')
    }
    else{
      addToCart(product_id, action)
    }


  })
}

function addToCart(p_id, acti){
 
  const data = {id:p_id, action: acti}
      let url = '/updatecart'
      fetch(url, {
          method: 'POST', // or 'PUT'
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
          },
          body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data =>{
            let cart = document.getElementById('cart')
            cart.innerHTML =  `<h4>${data.qty}</h4>`
            console.log(data)
          
        })
        .catch((error) => {
          console.error('Error:', error);
        });

}

let inputField = document.getElementsByTagName('input')
for(let i = 0; i<inputField.length; i++){
    inputField[i].addEventListener('change', updateQty)
}
function updateQty(e){
    let p_id = e.target.dataset.product
    let inputvalue = e.target.value
    console.log(p_id)
    const data = {id:p_id, val: inputvalue}
      let url = '/updatequantity'
      fetch(url, {
          method: 'POST', // or 'PUT'
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
          },
          body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data =>{
            
            console.log(data)
            e.target.parentElement.parentElement.children[4].innerHTML  = ` <h3>$${data.subtotal.toFixed(2)}</h3>`
            document.getElementById('total').innerHTML = `<h3>$${data.grandtotal.toFixed(2)}</h3>`
            let cart = document.getElementById('cart')
            
            cart.innerHTML =  `<h3>${data.quantity}</h3>`
        })
        .catch((error) => {
          console.error('Error:', error);
        });


}