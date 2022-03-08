python3 main_pretrain.py \
    --batch_size 64 \
    --epochs 400 \
    --model mae_vit_large_patch16 \
    --norm_pix_loss \
    --mask_ratio 0.75 \
    --epochs 800 \
    --warmup_epochs 40 \
    --blr 1.5e-4 --weight_decay 0.05 \
    --data_path data/herbarium/train_images \
    --anno_file  data/herbarium/train_metadata.json 


python3 main_pretrain.py    \
    --batch_size 64     \
    --epochs 400     \
    --model mae_vit_large_patch16     \
    --norm_pix_loss     \
    --mask_ratio 0.75     \
    --epochs 800     \
    --warmup_epochs 40     \
    --blr 1.5e-4 --weight_decay 0.05     \
    --data_path data/herbarium/train_images     \
    --anno_file  data/herbarium/train_metadata.json    \
    --world_size 8