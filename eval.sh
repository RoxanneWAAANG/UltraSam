export PYTHONPATH=$PYTHONPATH:.

mim train mmdet configs/UltraSAM/UltraSAM_full/UltraSAM_point_refine.py --gpus 4 --launcher pytorch --work-dir ./work_dirs/UltraSam
mim test mmdet configs/UltraSAM/UltraSAM_full/UltraSAM_point_refine.py --checkpoint ./work_dirs/UltraSam/iter_30000.pth
mim test mmdet configs/UltraSAM/UltraSAM_full/UltraSAM_box_refine.py --checkpoint ./work_dirs/UltraSam/iter_30000.pth


mim train mmpretrain configs/UltraSAM/UltraSAM_full/downstream/classification/BUSBRA/resnet50.py \
    --work-dir ./work_dirs/classification/BUSBRA/resnet
mim train mmpretrain configs/UltraSAM/UltraSAM_full/downstream/classification/BUSBRA/MedSAM.py \
    --work-dir ./work_dirs/classification/BUSBRA/MedSam
mim train mmpretrain configs/UltraSAM/UltraSAM_full/downstream/classification/BUSBRA/SAM.py \
    --work-dir ./work_dirs/classification/BUSBRA/Sam
mim train mmpretrain configs/UltraSAM/UltraSAM_full/downstream/classification/BUSBRA/UltraSam.py \
    --work-dir ./work_dirs/classification/BUSBRA/UltraSam
mim train mmpretrain configs/UltraSAM/UltraSAM_full/downstream/classification/BUSBRA/ViT.py \
    --work-dir ./work_dirs/classification/BUSBRA/ViT

mim train mmdet configs/UltraSAM/UltraSAM_full/downstream/segmentation/BUSBRA/resnet.py \
    --work-dir ./work_dirs/segmentation/BUSBRA/resnet
mim train mmdet configs/UltraSAM/UltraSAM_full/downstream/segmentation/BUSBRA/UltraSam.py \
    --work-dir ./work_dirs/segmentation/BUSBRA/UltraSam_3000
mim train mmdet configs/UltraSAM/UltraSAM_full/downstream/segmentation/BUSBRA/SAM.py \
    --work-dir ./work_dirs/segmentation/BUSBRA/SAM
mim train mmdet configs/UltraSAM/UltraSAM_full/downstream/segmentation/BUSBRA/MedSAM.py \
    --work-dir ./work_dirs/segmentation/BUSBRA/MedSAM