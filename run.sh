python main.py --dataset 64_3c --input_height=64 --output_height=64 --input_fname_pattern="*.jpg" \
--batch_size 64 \
--epoch 100 \
--learning_rate 0.0002 \
--label1_dim 10 --label2_dim 10 \
--label2_path ./data/3meta/style.pkl --label1_path ./data/3meta/genre.pkl \
--train
