

operators = ['plus', 'minus', 'times', 'divided by']
transcript = ""
duration = 10
running = true
test = -1;

let soundCorrect = new Audio ("right.wav")
let soundIncorrect = new Audio ("wrong.wav")

numCorrect = 0
numIncorrect = 0


function countdown(duration) {
    const timer = setInterval(() => {
      if (seconds > 0) {
        console.log()
        seconds--
      } else {
        running = false
        console.log("Countdown completed.")
        clearInterval(timer)
      }
    }, 1000);
  }
  
  function listen() {
    SpeechRecognition.
    
  }

function speak(num1, num2, i){
        let firstNum = new SpeechSynthesisUtterance(String(num1))
        speechSynthesis.speak(firstNum);

        let op  =  new SpeechSynthesisUtterance(operators[i])
        speechSynthesis.speak(op);

        let secondNum = new SpeechSynthesisUtterance(String(num2))
        speechSynthesis.speak(secondNum)
 }


function genNumber(){
    num1Addition = Math.floor(Math.random() * (100 - 2 + 1)) + 2;
    num2Addition = Math.floor(Math.random() * (100 - 2 + 1)) + 2;

    num1Multiplication = Math.floor(Math.random() * (12 - 2 + 1)) + 2;
    num2Multiplication = Math.floor(Math.random() * (100 - 2 + 1)) + 2;

    op = Math.floor(Math.random() * (4 - 2 + 1)) + 0;
    if (op == 0){
        test = num1Addition + num2Addition  
        speak(num1Addition, num2Addition, 0)
    }    
    else if(op == 2){
        test = num1Multiplication * num2Multiplication

        speak(num1Multiplication, num2Multiplication, 2)

    } else if(op == 1){
        if (num1Addition > num2Addition){
            test = num1Addition - num2Addition
            speak(num1Addition, num2Addition, 1)
                } else{
                    speak(num2Addition, num1Addition, 1)
                }
    }else{
        if(num2Multiplication % num1Multiplication != 0){
            while (num2Multiplication % num1Multiplication != 0){
                console.log("here4")
                num1Multiplication = Math.floor(Math.random() * (12 - 2 + 1)) + 2;
                num2Multiplication = Math.floor(Math.random() * (100 - 2 + 1)) + 2;
            }
           test = num2Multiplication / num1Multiplication
           speak(num2Multiplication, num1Multiplication, 3)
        }
        
    }        

}

function main(){

}

    
    