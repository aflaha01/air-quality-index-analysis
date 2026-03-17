function generateRandom() {
    document.querySelectorAll("input[type='number']").forEach(input => {
        input.value = (Math.random() * 100).toFixed(2);
    });
}
