// In charge of the processing wheel 
function showWheel(){
    const load_text = document.querySelector('.load-text');
    const load_text_container = document.querySelector('.load-text-container');
    const result_container = document.querySelector('.result-container');
    const text = document.createTextNode("Processing ...")
    const dual_ring_container = document.querySelector('.dual-ring-container');

    load_text.appendChild(text)
    result_container.remove();

    load_text.style.cssText = 
    'font-size:26px;font-family:system-ui;margin-left:12px;padding-bottom:7px';
    load_text_container.style.cssText = 
    'display:flex;align-items:center;justify-content:center;'
    dual_ring_container.style.cssText = 
    'opacity:1;';
}

// Disable button after user pressed submit
function disableButton(){
    document.getElementById("btn-1").disabled = true;
    document.getElementById("form-container").submit()
}

// When the server result is error change css style to red font
function error(){
    const result_content = document.querySelector('.result-content')
    const result_title = document.querySelector('.result-title')

    result_content.style.cssText =
    'font-size:28px;font-family:system-ui;font-weight:normal;background-color:rgb(178, 255, 213);color:rgb(229, 0, 0);border-radius:15px;padding:25px 30px;min-height:250px;width:500px;'
    result_title.style.cssText = 
    'font-size:28px;font-weight:normal;margin:0px;color:rgb(61, 61, 61);'
}