/* import { useEffect, useState } from "react";

let recognition: any = null

if("webkitSpeecRecognition" in window){
    recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.lang="tr";
    
}

const useSpeechRecognition = () => {
    const [text, setText] = useState("");
    const [isListening, setIsListenig] = useState(false);

    useEffect(()=>{
        if(!recognition) return;

        recognition.onresult = (event)

    },[])
    
};

export default useSpeechRecognition; */