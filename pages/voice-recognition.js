import React from "react";
import Link from "next/link";
import Layout from "@/components/layout/Layout";
import PageHead from "@/components/layout/PageHead";
import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";

function VoiceRecognition() {
  const startListening = () =>
    SpeechRecognition.startListening({ continuous: true, language:'tr' });
  const { transcript, browserSupportsSpeechRecognition } =
    useSpeechRecognition();

  return (
    <>
      <Layout>
        <PageHead headTitle="Voice Recognition"></PageHead>
        <div>
          <h1 className="text-center text-primary">Ses Tanıma</h1>
        </div>
        <div>
          <div className="text-center p-2 m-2">
            <p>{transcript}</p>
            <button onClick={SpeechRecognition.abortListening} className="">
              start listening
            </button>
            <button onClick={SpeechRecognition.stopListening} className="">
              stop listening
            </button>
          </div>
        </div>
      </Layout>
    </>
  );
}

export default VoiceRecognition;
