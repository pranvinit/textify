const pinText = document.querySelectorAll(".pin_info")
const pin = document.querySelectorAll(".pinanchor")

const unpinText = document.querySelectorAll(".unpin_info")
const unpin = document.querySelectorAll(".unpinanchor")

const severity = document.querySelectorAll(".severityanchor")
const severityText = document.querySelectorAll(".severity_info")

for(let i = 0; i < pin.length; i++){
    pin[i].addEventListener('mouseover', () => {
        pinText[i].style.display = 'flex';
    })
    pin[i].addEventListener('mouseout', () => {
        pinText[i].style.display = 'none';
    })
}
for(let i = 0; i < unpin.length; i++){
    unpin[i].addEventListener('mouseover', () => {
        unpinText[i].style.display = 'flex';
    })
    unpin[i].addEventListener('mouseout', () => {
        unpinText[i].style.display = 'none';
    })
}

for(let i = 0; i < severity.length; i++){
    severity[i].addEventListener('mouseover', () => {
        severityText[i].style.display = 'flex';
    })
    severity[i].addEventListener('mouseout', () => {
        severityText[i].style.display = 'none';
    })
}