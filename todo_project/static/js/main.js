const handleSignUpForm = (evt) => {
    evt.preventDefault() 
    const formData = new FormData(evt.target);
    const formProps = Object.fromEntries(formData);
    console.log(formProps)
    
    axios.post('/signup', formProps).then((response)=>{
        let p = document.createElement("p")
        if(response["data"]["success"]){
            p.innerHTML ="Successfully created account!";
        }
        else{
            p.innerHTML = "Creation unsuccessful!";
        }
        p.classList.add("text-center")
        document.body.appendChild(p)
    })
}

const handleLogInForm = (evt) => {
    evt.preventDefault() 
    const formData = new FormData(evt.target);
    const formProps = Object.fromEntries(formData);
    console.log(formProps)
    
    axios.post('/login', formProps).then((response)=>{
         console.log(response)   
         window.location="/todos"
     })
}

const handleToDoForm = (evt) => {
    evt.preventDefault() 
    const formData = new FormData(evt.target);
    const formProps = Object.fromEntries(formData);
    console.log(formProps)
    
    axios.post('/todos/new', formProps).then((response)=>{
        console.log(response)
        window.location="/todos"
    })
}

const handleEditForm = (evt,id) => {
    evt.preventDefault() 
    const formData = new FormData(evt.target);
    const formProps = Object.fromEntries(formData);

    axios.post(`/todos/${id}/edit`, formProps).then((response)=>{
        console.log(response)
        window.location=`/todos/${id}`
    })
}