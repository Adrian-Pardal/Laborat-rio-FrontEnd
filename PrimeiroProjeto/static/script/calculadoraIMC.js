const form = document.getElementById('form');


form.addEventListener('submit', function(event){

    event.preventDefault();

    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;

    const bmi = (weight / (height * height)).toFixed(2);

    if (!isNaN(bmi)) {
        const value = document.getElementById('value');
        let description = '';}

    value.classList.add('attention');

    document.getElementById('infos').classList.remove('hidden');


    if (bmi <18.5) {
        description = "Esta Abaixo Do Seu Peso Ideal Cuidado!!";
    }   else if (bmi >= 18.5 && bmi <= 25){
        description = "Seu Peso Esta Ideal!!";
        value.classList.remove("attention");
        value.classList.add("normal");
    }   else if (bmi > 25 && bmi <= 30){
        description = "Preste Atenção Você Esta Com Sobrepeso";
    }   else if (bmi > 30 && bmi <= 35){
        description = "Cuidado! Você Está Com Obesidade Moderada";
    }   else if (bmi > 35 && bmi <= 40){
        description = "Você Tem Obesidade Several, Consulte Um Profissional De Saude";
    }   else {
        description = "Obesidade Mórbida - Consultar um profissional de saúde imediatamente.";
    }

    value.textContent = bmi.replace('.',',' );
    document.getElementById('description').textContent = description;

});

form.addEventListener('keypress', function(event) {
    if (event.key === 'press') {
        document.getElementById('#calculate').click();
    }
});