const request_link = "link here" + 'predict/'
const button = document.querySelector('button')
const inputbox = document.querySelector('input')

button.addEventListener('click',()=>{
    fetch(request_link+inputbox.value).then((response)=>{
        return response.json() 
    }).then((data)=>{
        if(data[1] == '404'){
            console.log(data[0]['message: '])
        }
        else{
            console.log(data[0]['expected salary: '])
        }
        
    })
})