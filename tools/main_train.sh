nohup python3 -m torch.distributed.launch --nproc_per_node=8 main_pretrain.py     \
    --batch_size 64   --epochs 400         \
    --model mae_vit_large_patch16         \
    --norm_pix_loss     --mask_ratio 0.75 \
    --warmup_epochs 40   --blr 1.5e-4 --weight_decay 0.05         \
    --data_path data/herbarium/train_images         \
    --anno_file  data/herbarium/train_metadata.json        \
    --world_size 8 \
    2>&1 > nohup400ep.out &