const panels = document.querySelectorAll('.panel');

//console.log(panels);
//console.log(panels[0]);

panels.forEach((panel) => {
    //console.log(panel)
    panel.addEventListener('click', () => {
        removeActiveClasses();
        panel.classList.add('active');
    })
});

function removeActiveClasses(){
    panels.forEach((panel) => {
        panel.classList.remove('active');
    });
}