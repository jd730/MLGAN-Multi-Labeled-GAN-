python main.py --dataset 5c64 --input_height=64 --output_height=64 --input_fname_pattern="*.jpg" \
--batch_size 64 \
--epoch 50 \
--learning_rate 0.0002 \
--label1_dim 5 --label2_dim 5 \
--label1_path ./data/5c64_meta/style.pkl --label2_path ./data/5c64_meta/genre.pkl \
--weight 0.01
--train
