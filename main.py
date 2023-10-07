import BrailleGenerator as BG;
import AudioToText as ATT;

if __name__ == '__main__':
    text = ATT.speech_to_text("hindi.wav","hi-IN")
    print(text)
    res = BG.generateBrailleCode(text)
    print(res)