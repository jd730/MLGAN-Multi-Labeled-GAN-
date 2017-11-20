python main.py --dataset 128mlgan_data --input_height=64 --output_height=64 --input_fname_pattern="*.jpg" \
--batch_size 64 \
--epoch 100 \
--train \
--learning_rate 0.0002 \
--label1_dim 10 --label2_dim 10 \
--label2_path ./data/128mlgan_meta/style.pkl --label1_path ./data/128mlgan_meta/genre.pkl
