rm /opt/tiger/minist/mae_herbarium2022/pretrain_dir/*
python submitit_pretrain.py \
    --job_dir pretrain_dir \
    --ngpus 8 \
    --nodes 1 \
    --batch_size 32 \
    --model mae_vit_large_patch16 \
    --norm_pix_loss \
    --mask_ratio 0.75 \
    --epochs 800 \
    --warmup_epochs 40 \
    --blr 1.5e-4 --weight_decay 0.05 \
    --data_path data/herbarium/train_images \
    --anno_file  data/herbarium/train_metadata.json