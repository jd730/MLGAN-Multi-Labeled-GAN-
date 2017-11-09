python main.py --dataset Realism --input_height=64 --input_fname_pattern="*.png" --train
python main.py --dataset Realism --input_height=64 --input_fname_pattern="*.png" --output_height=64
mv samples Realism_100
python main.py --dataset Rococo --input_height=64 --input_fname_pattern="*.png" --train
python main.py --dataset Rococo --input_height=64 --input_fname_pattern="*.png" --output_height=64
mv samples Rococo_100
python main.py --dataset Romanticism --input_height=64 --input_fname_pattern="*.png" --train
python main.py --dataset Romanticism --input_height=64 --input_fname_pattern="*.png" --output_height=64
mv samples Romanticism_100
python main.py --dataset Impressionism --input_height=64 --input_fname_pattern="*.png" --train
python main.py --dataset Impressionism --input_height=64 --input_fname_pattern="*.png" --output_height=64
mv samples Impressinism_100
python main.py --dataset Expressionism --input_height=64 --input_fname_pattern="*.png" --train
python main.py --dataset Expressionism --input_height=64 --input_fname_pattern="*.png" --output_height=64
mv samples Expressionism_100
