python main.py --dataset C --input_height=64 --output_height=64 --input_fname_pattern="*.jpg" \
--batch_size 16 \
--epoch 100 \
--train \
--learning_rate 0.0001 \
--label1_dim 15 --label2_dim 15 \
--label1_path ./data/mlgan_meta/style.pkl --label2_path ./data/mlgan_meta/genre.pkl
