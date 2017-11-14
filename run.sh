python main.py --dataset C_1725 --input_height=64 --output_height=64 --input_fname_pattern="*.jpg" \
--batch_size 64 \
--epoch 100 \
--train \
--learning_rate 0.0002 \
--label1_dim 3 --label2_dim 4 \
--label2_path ./data/3meta/style.pkl --label1_path ./data/3meta/genre.pkl
