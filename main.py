import BrailleGenerator as BG;
import AudioToText as ATT;
import BraillePad as BP;

if __name__ == '__main__':
    #text = ATT.speech_to_text("hindi.wav","hi-IN")
    text="hello"
    print(text)
    res = BG.generateBrailleCode(text)
    print(res)
    BP.run(res)
