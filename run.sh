python main.py --dataset total --input_height=64 --output_height=64 --input_fname_pattern="*.jpg" \
--batch_size 32 \
--label1_dim 15 --label2_dim 15 \
--crop \
--label1_path="./data/mlgan_meta/style.pkl" \
--label2_path="./data/mlgan_meta/genre.pkl" \
--train 
