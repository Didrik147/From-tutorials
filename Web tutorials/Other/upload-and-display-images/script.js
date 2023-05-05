const image_input = document.querySelector("#image_input")
var uploaded_image = "";

image_input.addEventListener("change", function(){
    //console.log(image_input.value)
    const reader = new FileReader();
    
    reader.addEventListener("load", () => {
        uploaded_image = reader.result;
        //console.log(uploaded_image)
        document.querySelector("#display_image").style.backgroundImage = `url(${uploaded_image})`
    });
    reader.readAsDataURL(this.files[0])
})