python main.py --dataset 3data_back --input_height=64 --output_height=64 --input_fname_pattern="*.jpg" \
--batch_size 64 \
--train \
--label1_dim 15 --label2_dim 15 \
--label1_path ./data/3meta/style.pkl --label2_path ./data/3meta/genre.pkl
