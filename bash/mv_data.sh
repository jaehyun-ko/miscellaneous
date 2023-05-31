#!/bin/bash
src_dirs=(
"/home/nas4/DB/speaker_verification/data/voxceleb2"
"/home/nas4/DB/speaker_verification/data_aug/musan_split"
"/home/nas4/DB/speaker_verification/data_aug/RIRS_NOISES/simulated_rirs"
)

dst_dirs=(
"/home/DB/speaker_verification/data/voxceleb2"
"/home/DB/speaker_verification/data_aug/musan_split"
"/home/DB/speaker_verification/data_aug/RIRS_NOISES/simulated_rirs"
)

for i in 0 1 2
do
    mkdir -p ${dst_dirs[i]} && rsync -avhP --stats --progress ${src_dirs[i]} ${dst_dirs[i]}
done
