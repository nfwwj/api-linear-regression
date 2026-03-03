const request_link = "https://xb616htq-5000.asse.devtunnels.ms/predict/"
const button = document.querySelector('button')
const inputbox = document.querySelector('input')

button.addEventListener('click',()=>{
    fetch(request_link+inputbox.value).then((response)=>{
        return response.json() // readble stream
    }).then((data)=>{
        if(data[1] == '404'){
            console.log(data[0]['message: '])
        }
        else{
            console.log(data[0]['expected salary: '])
        }
        
    })
})