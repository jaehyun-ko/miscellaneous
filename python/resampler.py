import torchaudio
from pathlib import Path
from tqdm.auto import tqdm
import argparse


# class AudioPreprocessor:

def down_sample(input_wav:str, output_wav:str, resample_sr:int):
    '''
    input_wav: input wav file path
    origin_sr: original sample rate
    resample_sr: resample sample rate
    '''    
    waveform, origin_sr = torchaudio.load(input_wav)
    resampler = torchaudio.transforms.Resample(orig_freq = origin_sr, new_freq = resample_sr)
    resample = resampler(waveform)
    torchaudio.save(output_wav, resample, resample_sr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='argument paser for resample datset.')
    parser.add_argument('--input_dir', type=str, default='default_dir', help='input wav file directory')
    parser.add_argument('--output_dir', type=str, default='replace_dir', help='output wav file directory')
    parser.add_argument('--resample_sr', type=int, default=16000, help='resample sample rate')
    args = parser.parse_args()
    
    input_dir = args.input_dir
    output_dir = args.output_dir
    resample_sr = args.resample_sr
    
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    input_files = input_path.glob('**/*.wav')
    for input_wav in tqdm(list(input_files), desc = "Resampling"):
        output_wav = Path(str(input_wav).replace(input_dir, output_dir))
        output_wav.parent.mkdir(parents=True, exist_ok=True)
        down_sample(input_wav, output_wav, resample_sr)
