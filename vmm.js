// function speak(text){
//     let utterance = new SpeechSynthesisUtterance(text)
//     let ss = new speechSynthesis
//     speechSynthesis.speak(utterance)
// }

function genNumber(){
    num1Addition = Math.random(2,100)
    num2Addition = Math.random(2,100)

    num1Multiplication = Math.random(2,12)
    num2Multiplication = Math.random(2,100)

    op =  Math.random(0,4)
    if (op == 0){
        test = num1Addition + num2Addition
        let utterance = new SpeechSynthesisUtterance(num1Addition);
        speechSynthesis.speak(utterance);

        utterance = new SpeechSynthesisUtterance(num2Addition);
        speechSynthesis.speak(utterance);
        
        engine.say(num1Addition)
        engine.say(operators[op])
        engine.say(num2Addition)
    }    
    else if(op == 2){
        test = num1Multiplication * num2Multiplication
        engine.say(num1Multiplication)
        engine.say(operators[op])
        engine.say(num2Multiplication)

    } else if(op == 1){
        if (num1Addition > num2Addition){
            test = num1Addition - num2Addition
            engine.say(num1Addition)
            engine.say(operators[op])
            engine.say(num2Addition)
                } else{
                    test = num2Addition - num1Addition
                    engine.say(num2Addition)
                    engine.say(operators[op])
                    engine.say(num1Addition)
                }
    }else{
        if (num2Multiplication % num1Multiplication != 0)
        while (num2Multiplication % num1Multiplication != 0)
            num1Multiplication = random.randrange(2,12)
            num2Multiplication = random.randrange(2,100)
        test = num2Multiplication / num1Multiplication
        engine.say(num2Multiplication)
        engine.say(operators[op])
        engine.say(num1Multiplication)
    }        

}

    
    